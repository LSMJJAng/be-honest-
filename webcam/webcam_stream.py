from flask import Flask, Response
import cv2
app = Flask(__name__)
video = cv2.VideoCapture(0)

@app.route('/')
def index():
    return "Default Message"

def gen(video):
    while True:
        success, image = video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()

        print('#' * 30)
        print(f'image: {image}')
        print('#' * 30)
        print(f'ret: {ret}')
        print('#' * 30)
        print(f'jpeg: {jpeg}')
        print('#' * 30)
        print(f'frame: {frame}')
        print('#' * 30)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        # yield frame

@app.route('/video_feed')
def video_feed():
    global video

    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame'
                    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2204, threaded=True)