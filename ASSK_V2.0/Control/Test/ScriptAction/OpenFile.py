# _*_ coding:UTF-8 _*_
from time import *
from path import *
from BaseAction.KeyboardAction import *
from BaseAction.MouseAction import *


# 打开指定的网页
def open_file(software_name = "", file_name = ""):
	if len(software_name) == 0 or len(file_name) == 0 :
		return

	win32api.ShellExecute(0, 'open', software_name, file_name, '', 1)      # 打开文件 


if __name__ == "__main__":
	open_file('notepad.exe', '1.txt')