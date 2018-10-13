# _*_ coding:UTF-8 _*_
from time import *
from path import *
from BaseAction.KeyboardAction import *
from BaseAction.MouseAction import *


# 当前窗口最小化
def shut_down():
	os.system("shutdown -s -t 60")


if __name__ == "__main__":
	shut_down()