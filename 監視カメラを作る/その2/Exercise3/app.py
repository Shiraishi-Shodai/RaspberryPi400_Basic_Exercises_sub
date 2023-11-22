from flask import render_template, Flask, Response
import cv2 as cv

app = Flask(__name__, template_folder="./templates")

def gen_frames():
    
   while True:
       camera = cv.VideoCapture(0)
       success, frame = camera.read()
       if not success:
           break
       else:
           #フレームデータをjpgに圧縮(ret: bool, buffer: ndarray)
           ret, buffer = cv.imencode('.jpg',frame)
           # bytesデータ化
           frame = buffer.tobytes()
           # カメラを解放
           camera.release()
            # yield 莫大な量の戻り値を小分けにして返すことが出来る
            # 新しいフレーム（画像）をブラウザに送信
           yield (b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        

@app.route('/video_feed')
def video_feed():
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

@app.route('/')
@app.route('/index')
def index():
   
   user = {'username': 'FZ50'}
   return render_template('index.html', title='home', user=user)

if __name__ == "__main__":
    app.run(debug=True, port=5000)