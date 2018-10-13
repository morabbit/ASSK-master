# _*_ coding:UTF-8 _*_
import win32api
import win32con
import win32gui
import time
from ctypes import *


# 鼠标移动
def mouse_move(x, y):
    windll.user32.SetCursorPos(x, y)


# 鼠标单击
def mouse_click(x=None, y=None):
    if not x is None and not y is None:
        mouse_move(x, y)
        time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


# 鼠标双击
def mouse_dclick(x=None, y=None):
    if not x is None and not y is None:
        mouse_move(x, y)
        time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


# 鼠标两点拖拽
def mouse_absolute(x, y, x2, y2):
    windll.user32.SetCursorPos(x, y)  # 鼠标移动到
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 左键按下
    time.sleep(0.2)
    mw = int(x2 * 65535 / 1920)
    mh = int(y2 * 65535 / 1080)
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE +
                         win32con.MOUSEEVENTF_MOVE, mw, mh, 0, 0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


# 鼠标多点拖拽
def mouse_move_press(path=[]):
    if len(path) == 0:
        return

    try:
        windll.user32.SetCursorPos(path[0][0], path[0][1])  # 鼠标移动到
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 左键按下
        time.sleep(0.2)
    except:
        return

    try:
        for point in path:
            mw = int(point[0] * 65535 / 1920)
            mh = int(point[1] * 65535 / 1080)
            win32api.mouse_event(
                win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, mw, mh, 0, 0)
            time.sleep(0.02)
    except:
        pass

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


# 鼠标滚轮
def mouse_wheel(step):
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, step, win32con.WHEEL_DELTA)


# 测试
if __name__ == "__main__":
    pass
