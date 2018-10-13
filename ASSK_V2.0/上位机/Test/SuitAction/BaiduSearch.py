# _*_ coding:UTF-8 _*_
from time import *
from path import *
from BaseAction.KeyboardAction import *
from BaseAction.MouseAction import *
from ScriptAction.OpenFile import *
from ScriptAction.OpenSoftWare import *
from ScriptAction.OpenWeb import *
from ScriptAction.ShutDown import *
from ScriptAction.WindowMax import *
from ScriptAction.WindowMin import *

# 打开指定的网页
def baidu_serach(text = ""):
	open_web('http://www.baidu.com')

	if len(text) == 0:
		return

	time.sleep(1)
	window_max()

	time.sleep(1)
	key_input(text)

	time.sleep(0.5)
	key_press("enter")

	time.sleep(0.5)
	key_press("enter")


if __name__ == "__main__":
	baidu_serach("meinv")