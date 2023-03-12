import pyautogui

if __name__ == '__main__':
    # pyautogui.screenshot('사진저장할 경로', region=(영역1, 영역2, 영역3, 영역4))
    # 추후에 부정행이에 속할경우 웹캠 위치에 맞게 region 설정한후 사진을 찍어서 slack dm img로 전달하도록 수정
    pyautogui.screenshot('/Users/sharekim_hangyuseong/Desktop/test.png')