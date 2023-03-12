import wx

def detect_dual_monitor_num() -> bool:
    app = wx.App()

    # To get the count of displays
    num_displays = wx.Display.GetCount()

    # 다중(외부) 모니터 감지되면 False 반환, 그렇지 아니하면 True 반환
    return True if num_displays == 1 else False

if __name__ == '__main__':
    monitor_num = detect_dual_monitor_num()