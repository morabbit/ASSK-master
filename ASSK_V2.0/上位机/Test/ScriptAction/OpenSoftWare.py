# _*_ coding:UTF-8 _*_
from time import *
from path import *
from BaseAction.KeyboardAction import *
from BaseAction.MouseAction import *


# 后台打开指定的软件
def open_software_in_back(software_name = ""):
	if len(software_name) == 0:
		return

	win32api.ShellExecute(0, 'open', software_name, '', '', 0)

# 前台打开指定的软件
def open_software_in_front(software_name = ""):
	if len(software_name) == 0:
		return
		
	win32api.ShellExecute(0, 'open', software_name, '', '', 1)


if __name__ == "__main__":
	# open_software_in_front('notepad.exe')
	open_software_in_front('C:\\Program Files\\ASAP 1.8\\bin\\ASAP.exe')