# !/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from UIModula.MainWindow import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MainWindow()  # 启动窗口线程
    w.setWindowTitle('ASSK')  # 设置窗口标题
    w.show()  # 显示窗口

    sys.exit(app.exec_())  # 主消息时间循环
