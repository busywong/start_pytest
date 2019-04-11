#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm
@file: test_module2.py
@time: 4/10/2019 11:45 PM
根据命令行选项控制跳过测试
"""


import pytest


def test_func_fast():
    pass


@pytest.mark.slow
def test_func_slow():
    pass


