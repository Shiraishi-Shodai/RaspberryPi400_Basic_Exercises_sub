# インポート (適宜pipでインストールする)
import imutils
import numpy as np
import cv2

# VideoCaptureをオープン
cap = cv2.VideoCapture(0)

# モデルを読み込む
prototxt = '/home/pi/python/RaspberryPi400_Basic_Exercises/顔認証装置を作る/tools/deploy.prototxt'
model = '/home/pi/python/RaspberryPi400_Basic_Exercises/顔認証装置を作る/tools/res10_300x300_ssd_iter_140000.caffemodel'
net = cv2.dnn.readNetFromCaffe(prototxt, model)

# カメラ画像を読み込み，顔検出して表示するループ
while True:
    ret, frame = cap.read()

    # カメラ画像を幅400pxにリサイズ
    img = imutils.resize(frame, width=400)
    (h, w) = img.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

    # 物体検出器にblobを適用する
    net.setInput(blob)
    detections = net.forward()

    for i in range(0, detections.shape[2]):
        # ネットワークが出力したconfidenceの値を抽出する
        confidence = detections[0, 0, i, 2]
        # confidenceの値が0.5以上の領域のみを検出結果として描画する
        if confidence > 0.5:
            # 対象領域のバウンディングボックスの座標を計算する
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            # バウンディングボックスとconfidenceの値を描画する
            text = "{:.2f}%".format(confidence * 100)
            y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.rectangle(img, (startX, startY), (endX, endY), (0, 0, 255), 2)
            cv2.putText(img, text, (startX, y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

    cv2.imshow("Face Detection", img)
    k = cv2.waitKey(1)&0xff
    if k == ord('s'):
        cv2.imwrite("./output.jpg", img) # ファイル保存
    elif k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
