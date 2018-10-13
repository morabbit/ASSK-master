# !/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
from pyqtgraph.Qt import QtCore
from Server.ASSKMgr import ASSKMgr


# 图标展现类
class ShowDataMgr(QtCore.QObject):
    def __init__(self, canvas, parent=None):
        # 父类方法
        super(ShowDataMgr, self).__init__(parent)

        # 获取要管理的界面对象
        self.canvas = canvas

        # 准备数据容器
        self.showDataList = np.array([])

        # 显示表格
        self.matplot = self.canvas.addPlot(title="气氛浓度(ppm)")
        self.matplot.plot(self.showDataList, pen=(200, 200, 200), symbolBrush=(255, 0, 0), symbolPen='w')

        # Call ASSKMgr start function
        ASSKMgr.start_serial_process()

        # 创建定时器
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(100)  # 每0.1秒更新一次图像

    # 更新数据接口
    def update_figure(self):
        # self.showDataList = np.append(self.showDataList, np.linspace(x, y))
        self.showDataList = ASSKMgr.showDataList
        curve = self.matplot.plot(pen=(200, 200, 200), symbolBrush=(255, 0, 0), symbolPen='w')
        curve.setData(self.showDataList)

    # 更新数据接口
    def test_update_figure(self):
        # self.__ShowDataList = np.random.normal(size=100)
        self.showDataList = np.append(self.showDataList, np.random.normal(size=1))
        curve = self.matplot.plot(pen=(200, 200, 200), symbolBrush=(255, 0, 0), symbolPen='w')
        curve.setData(self.showDataList)
