#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm Community Edition
@file: test_some_are_slow.py
@time: 2019/4/10 16:12
分析测试持续时间   --durations=num
"""

# content of test_some_are_slow.py
import time,pytest


def test_funcfast():
    time.sleep(0.1)


def test_funcslow1():
    time.sleep(0.2)


def test_funcslow2():
    time.sleep(0.3)


if __name__ == '__main__':
    pytest.main(['--durations=4','test_some_are_slow.py'])


