# !/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog
from pyqtgraph.Qt import QtGui, QtCore
from UIModula.UIMainWindow import *
from UIModula.ShowDataMgr import *


# from Server import ASSKMgr


class MainWindow(QMainWindow, Ui_MainWindow):
    # server = ASSKMgr.ASSKMgr()  # 全局变量，实例化后台管理对象

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)  # 父类方法
        self.setupUi(self)  # 创建界面

        # 窗口最大化
        self.showMaximized()

        # 将plot放入
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.matplot = pg.GraphicsWindow(title="data plotting")
        self.gridLayout.addWidget(self.matplot, 0, 0, 0, 0)

        # 创建数据展示管理器，并将管理对象交给它
        self.shwoDataMgr = ShowDataMgr(self.matplot)

        # 三个按钮的信号与槽函数
        self.btnStart.clicked.connect(self.onBtnStartClickedSlot)
        self.btnStop.clicked.connect(self.onBtnStopClickedSlot)
        self.btnExport.clicked.connect(self.onBtnExportClickedSlot)
        self.btnShutDown.clicked.connect(self.onBtnShutDownSlot)

    # 程序退出事件，通知后台，关闭串口占用
    def closeEvent(self, event):
        return
        # self.server.cancel_seiral_occupy()

    # 开始监控（调用后台）
    @QtCore.pyqtSlot()
    def onBtnStartClickedSlot(self):
        return
        # self.server.start_serial_process()

    # 暂停监控（调用后台）
    @QtCore.pyqtSlot()
    def onBtnStopClickedSlot(self):
        return
        # self.server.cancel_seiral_process()

    # 导出数据（调用后台）
    @QtCore.pyqtSlot()
    def onBtnExportClickedSlot(self):
        self.onBtnStopClickedSlot()  # 先暂停，再导出
        file_name = QFileDialog.getSaveFileName(self, "导出路径", "C://Users//Administrator//Desktop", "CSV files(*.csv)")
        print(file_name)

    # 关机
    @QtCore.pyqtSlot()
    def onBtnShutDownSlot(self):
        os.system("shutdown -s -f -t 0")  # 调用系统命令，立即关机
