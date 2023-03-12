import time

# 시험 중 응시자 화면에 검출되면 안되는 물품 list
ban_list = [
    'cell phone', 'book', 'monitor', 'tvmonitor', 'tv'
]

# 온라인 시험 중에는 응시자의 화면에 무조건 1명만 인식이 되야한다.
# 객체 인식 list에서 사람의 개수가 1이 5초 동안 아니면 false를 반환
def check_person_num(label: list) -> bool:
    if label.count('person') != 1:
        start = time.time()
        if time.time() - start >= 5 and label.count('person') != 1:
            return False

    return True

def notify_person_num(label: list) -> str:
    if check_person_num(label) == False:
        if label.count('person') == 0:
            return "The screen doesn't recognize examinee"
        else:
            return "Multiple people are recognized on the screen."

# 온라인 시험 중에는 "핸드폰", "책", "모니터" 등은 검출되면 안된다.
# 부정행위 의심 목록이 하나라도 인식되면 해당 물품을 알려주는 함수
def check_ban_items(label: list) -> str:
    for item in ban_list:
        if item in label:
            return f'{item} recognized on screen.'