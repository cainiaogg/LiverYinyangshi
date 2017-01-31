# coding=utf-8
"""
自动点击屏幕功能，传入屏幕坐标，循环左键点击，每次循环间隔0.5s 适用于windows
"""
import autopy
import time
import pyHook
import sys
import pythoncom
import os
import threading


class Click(object):
    """
    点击类
    """

    def __init__(self, pos_in):
        """
        初始化函数，用来传入点击坐标
        :@param pos_in: 要点的屏幕坐标，list类型
        :return: None
        """
        self.pos_in = pos_in
        self.end_time = 3600

    def changeEndTime(self, end_time):
        """
        改变脚本刷的默认时间，默认时间为3600s，单位为second
        :@param end_time: int型，表示多少秒
        :return: None
        """
        self.end_time = endtime

    def clickCommon(self, x, y):
        """
        点击屏幕x，y位置，
        :@param x, y: 坐标
        :return: None
        """
        autopy.mouse.move(x, y)
        # autopy.mouse.smooth_move(x, y)
        autopy.mouse.click(1)

    def clickAll(self):
        """
        点击传入所有位置
        :@param: Null
        :return: None
        """
        while True:
            for item in self.pos_in:
                self.clickCommon(item[0], item[1])

    def onKeyboardEvent(self, event):
        """
        绑定键盘事件, 输入回车终止脚本
        :@param: event: 事件
        :return: True
        """
        print str(event.Key)
        if str(event.Key) == "Return":
            os._exit(0)
        return True

    def hook(self):
        """
        监听键盘
        :@param: Null
        :return: None
        """
        hm = pyHook.HookManager()
        hm.KeyDown = self.onKeyboardEvent
        hm.HookKeyboard()
        pythoncom.PumpMessages()

    def endShua(self):
        """
        在达到终止时间后终止脚本
        :@param: Null
        :return: None
        """
        time.sleep(self.end_time)
        os._exit(0)

    def begin(self):
        """
        脚本开始, 多线程。
        :@param: Null
        :return: None
        """
        threads = []
        t1 = threading.Thread(target=self.hook, args=())
        t2 = threading.Thread(target=self.clickAll, args=())
        t3 = threading.Thread(target=self.endShua, args=())
        threads.append(t1)
        threads.append(t2)
        threads.append(t3)
        for i in threads:
            i.start()
