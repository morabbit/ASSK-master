# _*_ coding:UTF-8 _*_
from BaseAction.MouseAction import *


class POINT(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]


# 点测试
def get_mouse_point():
    po = POINT()
    windll.user32.GetCursorPos(byref(po))
    return int(po.x), int(po.y)


# 移动到目标位置
def mouse_move_to_pos(x, y):
    mouse_move(x, y)


if __name__ == "__main__":
    mouse_move_to_pos(145, 60)
