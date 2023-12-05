from flask import Flask, Response, request, jsonify
from flask_cors import CORS
import cv2
from tkinter import filedialog
import shutil
import sys

# tkinterはデフォルトでCMSスレッド？らしいものを使用するらしいが、windowsはそれが使えないのでwindows仕様に合わせる
# sys.coinit_flags = 2 

app = Flask(__name__)
CORS(app)

cap = cv2.VideoCapture(0)
print(cap.isOpened())

# cap.set(cv2.CAP_PROP_SETTINGS, 1)
fmt = cv2.VideoWriter_fourcc(*'XVID')    
fps = 20.0
size = (640, 480)
writer = cv2.VideoWriter('video.avi', fmt, fps, size)

def gen_frames():
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        _, buffer = cv2.imencode('.jpg', frame)
        bytes_buffer = buffer.tobytes()

        """
        ストリーミング: インターネットを通じて、データを受信しながら音楽や動画を再生する方式(ここでは画像)
        """

        """
        送信内容
        # (\rはキャリッジリターンといい、カーソルの位置を行頭に移動する)
        # (\r\nはカーソルを行頭に戻して改行することを意味する)
        
            # --frame
            # Content-Type: image/jpeg
            # 
            # bytes_buffer
            #    
        """
        yield(b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + bytes_buffer + b'\r\n')
        
        # ここで一旦待機
        # 要素が要求される場面でその都度データを算出するので、メモリを多く消費しない
    
    
@app.route('/video_feed')
def video_feed():
    """HTTPレスポンスを返す(上二行がHTTPヘッダー, --frameから下が画像一枚に相当

    Returns:
        HTTP/1.1 200 OK
        content-type: multipart/x-mixed-replace; boundary=myboundary

        --frame
        Content-Type:image/jpeg
        
        bytes_buffer
        
        --frame
        Content-Type:image/jpeg
        
        bytes_buffer

        ...        
    """

    # Responseオブジェクトはジェネレータを指定できる
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')    

@app.route('/recoding', methods = ["GET", "POST"])
def recoding():
    if request.method == "GET":
        res = {'recoding': '録画を開始します'}
        print("録画を開始します")

    while cap.isOpened():

        ret, frame = cap.read()
        if ret:
            
            resize_frame = cv2.resize(frame, size)
            writer.write(resize_frame)

        if request.method == "POST":
            print(f'ここまで: {request.get_json()["message"]}')
            # 後処理
            writer.release()
            cap.release()
            
            res = {'recoding': '録画を停止しました'}
            print('停止しました')

            break


    return jsonify({"a": "b"})
    

@app.route('/save', methods=['POST'])
def save():

    if request.method == 'POST':
        file_name = request.get_json()['fileName']
        # print(f'到達: {file_name}')        
        folder_name = filedialog.askdirectory(initialdir=dir, title="ダウンロード先")
        save_path = folder_name + '/' + file_name + '.avi'

        shutil.move('video.avi', save_path)

        return jsonify({'Hello': "I'm save function"})
        
if __name__ == "__main__":
    app.run(port='5000', debug=True)