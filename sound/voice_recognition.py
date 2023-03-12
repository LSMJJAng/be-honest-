import speech_recognition as sr
import pyaudio

# 기기에 연결된 외부장치를 체크하고 반환하는 함수
def check_external_device():
    p = pyaudio.PyAudio()
    message = ''

    if p.get_device_count() != 2:
        for i in range(p.get_device_count()):
            message += f"{p.get_device_info_by_index(i)['name']} "
        return f'{message} is connected to your computer. Remove all external devices.'
    return


# 스피커를 활용해 음성인식을하고 텍스트로 변환해주는 함수
def convert_voice_to_text() -> str:
    # num = 0  # 외부 모니터 없이 돌릴 시,
    num = 1  # 외부 모니터 연결되었을 시,
    r = sr.Recognizer()

    with sr.Microphone(num) as source:
        r.adjust_for_ambient_noise(source, num)
        audio = r.listen(source)

    try:
        return "recoginigin voice: " + r.recognize_google(audio, language='en')
    except:
        pass