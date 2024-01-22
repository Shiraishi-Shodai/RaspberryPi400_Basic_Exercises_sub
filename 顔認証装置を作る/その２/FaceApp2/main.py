from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
from torchvision import datasets
from torch.utils.data import DataLoader
from PIL import Image
import cv2
import time
import os
import matplotlib.pyplot as plt

mtcnn0 = MTCNN(image_size=240, margin=0, keep_all=False, min_face_size=40) # 画像から人の顔を一つ検出するモデル
mtcnn = MTCNN(image_size=240, margin=0, keep_all=True, min_face_size=40) # 画像から全員の顔を検出するモデル
resnet = InceptionResnetV1(pretrained='vggface2').eval() # InceptionResnetV1モデルをVGGFace2データセットで事前に訓練済みの重みで初期化

# データを読み込み
dataset = datasets.ImageFolder('./data')
# ラベルをキー、フォルダ名を値とした辞書を作成
idx_to_class = {i:c for c,i in dataset.class_to_idx.items()}

def collate_fn(x):
    return x[0]

# データセットのバッチを表すイテレータを返す(画像データはpillow.Image型)
loader = DataLoader(dataset, collate_fn=collate_fn)
    
name_list = [] # 既知の人物名
embedding_list = [] # 既知の顔の特徴

for img, idx in loader:
    face, prob = mtcnn0(img, return_prob=True)

# mtcnnモデルが顔を検出していて、それが人間の顔である確率が92%以上のとき
    if face is not None and prob > 0.92:
        emb = resnet(face.unsqueeze(0)) # 画像から抽出された高次元の特徴を表すベクトルのテンソルを返す(512次元)
        embedding_list.append(emb.detach()) # detachは同一デバイス上に新しいテンソルを作成する。勾配の計算グラフからは切り離される
        name_list.append(idx_to_class[idx]) # 検出した顔の人物を追加

# 既知のデータを保存
data = [embedding_list, name_list]
torch.save(data, 'data.pt')

load_data = torch.load('data.pt')
embedding_list = load_data[0]
name_list = load_data[1]

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        print('画像を取得出来ませんでした')
        break
    
    img = Image.fromarray(frame)
    # 4次元の顔を切り取ったtensorと確信率を取得
    img_cropped_list, prob_list = mtcnn(img, return_prob=True)
    if img_cropped_list is not None:
        boxes, score = mtcnn.detect(img) # バウンディングボックスと顔の確信度を取得

        for i, prob in enumerate(prob_list):
            if prob > 0.9:
                emb = resnet(img_cropped_list[i].unsqueeze(0)).detach()
                
                dist_list = [] # 既知の顔とカメラで取得した顔のユークリッド距離を持つリスト
                
                for idx, emb_db in enumerate(embedding_list):
                    dist = torch.dist(emb, emb_db).item() # 既知の特徴のテンソルと、カメラで取得した顔の特徴のテンソルのユークリッド距離を取得(小さいほど類似していると言える)
                    dist_list.append(dist)
                
                min_dist = min(dist_list) # 最も小さい距離を取得
                min_dist_idx = dist_list.index(min_dist) # 小さい距離のインデックスを取得
                name = name_list[min_dist_idx] # 最も類似していると判断した顔の名前を取得
                
                box = boxes[i] # 顔の矩形の左上隅と右下隅の座標を取得
                box = list(map(lambda x: int(x), box)) # cv2.rectangleやputTextで座標を指定するときは、int型である必要があるので、座標をfloat型からint型に変換
                
                if min_dist < 0.8:
                    frame = cv2.putText(frame, name+ ' '+str(min_dist), (box[0], box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),1, cv2.LINE_AA)
                
                frame = cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), 2)
    
    cv2.imshow('img', frame)
    
    if cv2.waitKey(1) % 256 == 27: # escapeキー
        break
    
cap.release()
cv2.destroyAllWindows()
                
                
                
                
                
                
                
    
    
    
    