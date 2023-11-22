import cv2

# ビデオキャプチャの取得
cap = cv2.VideoCapture(0)
# コーデック（fourcc）の設定
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# 動画ファイルの設定（保存先、FPS、サイズ）
video = cv2.VideoWriter('C:/Users/shodai/Desktop/RaspberryPi400_Basic_Exercises/監視カメラを作る/その2/Exercise3/test/output.avi', fourcc, 20.0, (640,480))
# 動画の読み込みに問題がない限り処理を継続する
while(cap.isOpened()):
    # Bool値とキャプチャ画像を変数に格納
    ret, frame = cap.read()
    if ret==True:
        # リサイズを行う
        frame = cv2.resize(frame, (640,480))
        # フレームの書き込み（保存）
        video.write(frame)
        # 録画中の映像（画像）を表示
        cv2.imshow('recoding', frame)
        # qが押されたら録画を終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# 終了処理
cap.release()
video.release()
cv2.destroyAllWindows()