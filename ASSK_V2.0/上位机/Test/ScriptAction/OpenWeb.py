# _*_ coding:UTF-8 _*_
from time import *
from path import *
from BaseAction.KeyboardAction import *
from BaseAction.MouseAction import *


# 打开指定的网页
def open_web(web_addr_name = ""):
	if len(web_addr_name) == 0:
		return

	try:
		win32api.ShellExecute(0, 'open', web_addr_name, '', '', 1)   # 打开网页 
	except:
		print("the web cannot to be opened!!!")


if __name__ == "__main__":
	open_web('http://www.baidu.com')