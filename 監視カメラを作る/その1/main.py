import cv2

camera = cv2.VideoCapture(0)
print(camera.isOpened())

while True:
    '''
    frame(numpy.ndarray): 1フレームの映像
    ret: 取得が成功したかどうかのbool値
    '''
    ret, frame = camera.read()
    cv2.imshow('camera', frame)

    # cv2.waitKey: キーが押されるまで処理を待つ。戻り値は32ビットの整数
    # cv2.waitKey(1)は1ミリ秒待つ
    # cv2.waitKey(0)はキーが押されるまで処理を待つ
    
    # 0xFF: 8ビットの2進数の最大値
    # ord: 引数に指定した文字列をUnicodeで表した値を返却
    
    # cv2.waitKey(1)と0xFFの論理積を取り、下位８ビットがUnicodeでqを表した値と等しいとき
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release() # カメラを解放
cv2.destroyAllWindows() # すべてのOpenCVウィンドウを閉じます。

# print(ord('q'))
# print(type(ord('q')))
# print(0xFF)
# print(type(0xFF))
# print(cv2.waitKey(1) & 0xFF)