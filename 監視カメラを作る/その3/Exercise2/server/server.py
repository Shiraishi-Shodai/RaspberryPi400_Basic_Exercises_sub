from flask import Flask, Response, request, jsonify
from flask_cors import CORS
import cv2

app = Flask(__name__)
CORS(app)

cap = cv2.VideoCapture(0)
fmt = cv2.VideoWriter_fourcc(*'XVID')    
fps = 20.0
size = (640, 480)
writer = cv2.VideoWriter('video.avi', fmt, fps, size)

def gen_frames():
    while True:
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
    
    cap.release()
    
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

    print('ここまで')
    if request.method == "GET":
        res = {'recoding': '録画を開始します'}
        print(f"録画を開始します")

    while True:
        if request.method == "POST":
            
            writer.release()
            cap.release()
            res = {'recoding': '録画を停止しました'}
            print(f'受け取ったデータ{request.get_json()}')
            print(f"録画を停止しました")
            break

        ret, frame = cap.read()
        if not ret:
            break
        
        resize_frame = cv2.resize(frame, size)
        writer.write(resize_frame)

    return jsonify(res)
    
if __name__ == "__main__":
    app.run(port='5000', debug=True)