#/usr/bin/env python
# -*- coding: utf-8 -*-
import threading

class MyThread(threading.Thread):
    """
    属性:
    target: 传入外部函数, 用户线程调用
    args: 函数参数
    """
    def __init__(self, target, args):
        super(MyThread, self).__init__()  #调用父类的构造函数 
        self.target = target
        self.args = args

    def run(self) :
        self.target(self.args)