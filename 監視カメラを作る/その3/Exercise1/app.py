"""プログラムを起動して5秒間もしくはESCキーを押すまでの間の動画をファイルに保存するプログラムを作成する"""

import cv2
import time

cap = cv2.VideoCapture(0)
# 保存時のフォーマット
fmt = cv2.VideoWriter_fourcc(*'XVID')
# 一秒間に取得する枚数
fps = 20.0
# 画像サイズ
size = (640, 480)

writer = cv2.VideoWriter("/home/pi/python/RaspberryPi400_Basic_Exercises/監視カメラを作る/その3/Exercise1/video.avi", fmt, fps, size)

start = time.time()
print(f'{"start time".ljust(10)}: {time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(start))}')
end = time.time() + 5
print(f'{"end time".ljust(10)}: {time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(end))}')

    
while True:

    ret, frame = cap.read()
    if not ret:
        break

    resize_frame = cv2.resize(frame, size)
    writer.write(resize_frame)
    cv2.imshow("WebCam", frame)
    now = time.time() # 現在時刻を取得

    # escapeキーを押されたとき、または実行開始から5秒経過した時、録画を停止する
    if cv2.waitKey(1) == 27 or now >= end:

        print(f'{"now".ljust(10)}: {time.strftime("%Y/%m/%d %H:%M:%S")}')
        break

writer.release()
cap.release()
cv2.destroyAllWindows()