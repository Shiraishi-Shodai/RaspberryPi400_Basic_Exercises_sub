"""GUIを使って、保存ファイル名を指定でき、ボタンを押すとカメラの映像を指定したファイル名で保存するプログラムを作成する"""

from flask import render_template, Flask, Response, request
import cv2
import sys

app = Flask(__name__, template_folder="./templates", static_folder="./static")

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cap.set(cv2.CAP_PROP_FPS, 20.0)           # カメラFPSを20FPSに設定(1秒間に20枚表示)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300) # カメラ画像の横幅を300に設定
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 200) # カメラ画像の縦幅を200に設定

print(f'ここです: {cap.isOpened()}')

def gen_frames():
   '''
   画像を取得し
   
   :param: なし
   :type: なし
   :return: 新しい画像
   :rtype: generator
   '''
   while True:
       ret, frame = cap.read()
       if not ret:
           break
       else:           
           #フレームデータをjpgに圧縮(ret: bool, buffer: ndarray)
           ret, buffer = cv2.imencode('.jpg',frame)
           # bytesデータ化
           frame = buffer.tobytes()

            # yield 莫大な量の戻り値を小分けにして返すことが出来る
            # 新しいフレーム（画像）をブラウザに送信
       yield (b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
   cap.release()

@app.route('/video_feed')
def video_feed():
    '''
    画像をストリーミング
    
    :param: なし
    :type: なし
    :return: 画像情報
    :rtype: レスポンスオブジェクト
    '''
    # HTTPレスポンス
   #imgタグに埋め込まれるResponseオブジェクトを返す
    # デフォルトでは、ResponseオブジェクトはHTMLのmimetypeを持ちます。つまり、デフォルトのContent-Typeヘッダーは"text/html"に設定されています。
    # mimetype='multipart/x-mixed-replace; boundary=frame'は、HTTPレスポンスのContent-Typeヘッダーを設定します。
    # このヘッダーは、レスポンスの形式をブラウザに伝えます。multipart/x-mixed-replaceは、マルチパートレスポンスの各部分が前の部分を置き換えることを示します。これにより、ブラウザは新しい画像フレームを受信するたびに、前のフレームを新しいフレームで置き換え、リアルタイムのビデオストリームを表示します。

    # boundary: HTTPレスポンスの情報を1つずつ区別するために用いる
    '''
    例)
    
    Content-Type: multipart/form-data; boundary=aBoundaryString
    (マルチパート文書全体に関連付けられる、他のヘッダー)

    (データ)
    --aBoundaryString
    Content-Disposition: form-data; name="myField"

    (データ)
    --aBoundaryString
    (サブパート)
    --aBoundaryString--
    '''

    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture')
def capture():
    '''
    picuture.jpgという仮の名前で画像を保存
    
    :param: なし
    :type: なし
    :return: HTMLファイル
    '''
    ret, frame = cap.read()
    capture_error = ""

    if not ret:
        capture_error="キャプチャーエラー"
    else:
        cv2.imwrite(r"/home/pi/python/RaspberryPi400_Basic_Exercises/監視カメラを作る/その2/Exercise3/static/img/picture.jpg", frame)

    return render_template('capture.html', capture_error=capture_error)

@app.route('/save', methods=["POST"])
def save():
    '''
    入力された値でファイルを保存(保存先はその時、自分がいるディレクトリの直下)
    
    :param: なし
    :type: なし
    :return: なし
    :rtype: なし
    '''
    if request.method == "POST":
        img = cv2.imread(r"/home/pi/python/RaspberryPi400_Basic_Exercises/監視カメラを作る/その2/Exercise3/static/img/picture.jpg")    
        file_name = request.form["file_name"] + ".jpg"
        cv2.imwrite(file_name, img)
        
        print('アプリケーションを終了します')
        cap.release()
        sys.exit(0)

@app.route('/')
@app.route('/index')
def index():
   
   return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5000)