# coding=utf-8

import serial
import serial.tools.list_ports
from time import sleep

SYSTEM_COM1 = "com1"
SYSTEM_COM2 = "com2"


class SerialCommunication:
    y = None

    def __init__(self):
        self.service = None
        self.ports = list()
        self.receivedData = list()
        self.get_com_list()   # 获取串口

    def initialize(self, name, baud_rate=9600):
        self.service = serial.Serial(self.ports[0], baud_rate, timeout=0.5)
        if self.service.isOpen() is False:
            raise (Exception, "open com error")

        print(name + self.ports[0] + "open success !")

    def get_com_list(self):
        com_list = list(serial.tools.list_ports.comports())
        if len(com_list) <= 0:
            raise (Exception, "The Serial port can't find!")
        
        self.ports = [port[0] for port in com_list if port[0] not in (SYSTEM_COM1, SYSTEM_COM2)]

    def receive(self):
        serialData = ""
        while True:
            sleep(0.5)
            serialData = self.service.read_all()
            if serialData != "":
                break

        return serialData

    def parse_origin_data(self, origin):
        if not isinstance(origin, str):
            return None

        dataList = origin.split("\n")
        count = len(dataList)
        dataIndex = 0

        while dataIndex < count:
            if dataIndex == count - 1 and dataList[dataIndex].endswith("\r") is False:
                return dataList[dataIndex]

            self.receivedData.append(dataList[dataIndex])
            dataIndex += 1

        return None

    def read_serial_data(self):
        while True:
            data = ""
            data = data + str(self.receive(), encoding = "utf8")  
            fragmentaryData = self.parse_origin_data(data)
            if fragmentaryData is not None:
                data = fragmentaryData
                self.y = data

    def cancel_seiral_occupy(self):
        self.service.close()
