# _*_ coding:UTF-8 _*_
from time import *
from path import *
from BaseAction.KeyboardAction import *
from BaseAction.MouseAction import *


# 当前窗口最小化
def window_min():
	keys_press(["win", "down_arrow"])


if __name__ == "__main__":
	window_min()