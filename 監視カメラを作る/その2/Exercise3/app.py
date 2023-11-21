from flask import Flask, render_template
import cv2

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    if ret:
        while True:
            
            cv2.imshow("camera", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        camera.release()
        cv2.destroyAllWindows()
    
    return "Hello"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
