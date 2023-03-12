# from webcam.function_merge_run import merge_detection
from GazeTracking.gaze_tracking import GazeTracking
from webcam.function_merge_run import merge_detection, yield_webcam, pre_headpose_detection

from etc.check_run_process import notify_processing_app_name
from sound.voice_recognition import check_external_device, convert_voice_to_text

import argparse
import cv2

from flask import Flask, render_template, flash, Response

app = Flask(__name__)

@app.route("/")
def mainpage():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login/login.html')

################## ko ver
@app.route("/preparation")
def preparation():
    return render_template('Preparation.html')

@app.route("/caution1")
def caution1():
    return render_template('caution1.html')

@app.route("/caution2")
def caution2():
    return render_template('caution2.html')

################# en ver
@app.route("/preparations_en")
def preparation_en():
    return render_template('preparations_en.html')

@app.route("/precautions_en")
def precautions_en():
    return render_template('precautions_en.html')

@app.route("/precautions2_en")
def precautions2_en():
    return render_template('precautions2_en.html')

@app.route("/ai_list_en")
def ai_list_en():
    return render_template('ai_list_en.html')

@app.route("/ai_list2_en")
def ai_list2_en():
    return render_template("ai_list2_en.html")

# 시험 시작
@app.route("/test")
def test():
    # # 금지 목록중에 속한 어플리케이션이 활성화중이라면
    # if notify_processing_app_name():
    #     # 끄라고 웹에서 알림창 띄어줌
    #     flash(notify_processing_app_name())
    #     return render_template('precautions2_en.html')
    # # 외부 기기, 장치 등이 연결된 경우
    # if check_external_device():
    #     flash(check_external_device())
    #     return render_template('precautions2_en.html')
    global cap, isVideo, hps, out

    return Response(
        yield_webcam(cap, isVideo, hpd, out),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

if __name__ == "__main__":
    # gaze tracking parameter
    gaze = GazeTracking()
    webcam = cv2.VideoCapture(0)
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', metavar='FILE', dest='input_file', default=None,
                        help='Input video. If not given, web camera will be used.')
    parser.add_argument('-o', metavar='FILE', dest='output_file', default=None, help='Output video.')
    parser.add_argument('-wh', metavar='N', dest='wh', default=[720, 480], nargs=2, help='Frame size.')
    parser.add_argument('-lt', metavar='N', dest='landmark_type', type=int, default=1, help='Landmark type.')
    parser.add_argument('-lp', metavar='FILE', dest='landmark_predictor',
                        default='../Headpose_Detection/model/shape_predictor_68_face_landmarks.dat',
                        help="Landmark predictor data file.")
    # headpose detection parameter를 dict 사전형태로 모은다.
    args = vars(parser.parse_args())
    cap, isVideo, hpd, out = pre_headpose_detection(args)

    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(host="0.0.0.0", port="9999", debug=False)