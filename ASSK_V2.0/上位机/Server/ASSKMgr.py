# coding=utf8


import threading
import datetime
from SerialModula.SerialCommunication import SerialCommunication
import numpy as np


class ASSKMgr:
    s = SerialCommunication()   # 实例化串口通讯类
    fetch_x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    fetch_y = s.y
    showDataList = np.array([])

    @classmethod
    def __init__(cls):
        cls.s.initialize("ASSK_Process")
        thd = threading.Thread(target=cls.fetch_serial_data)
        thd.start()

    @classmethod
    def fetch_serial_data(cls):
        cls.s.read_serial_data()

    @classmethod
    def flash(cls):
        cls.showDataList = np.append(cls.showDataList, np.linspace(int(cls.fetch_x), int(cls.fetch_y)))

    @classmethod
    def start_serial_process(cls):
        global timer
        timer = threading.Timer(0.1, cls.flash)
        timer.start()

    @classmethod
    def cancel_seiral_process(cls):
        timer.cancel()

    @classmethod
    def cancel_seiral_occupy(cls):
        cls.s.cancel_seiral_occupy()
