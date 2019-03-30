#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm
@file: test_calc.py
@time: 3/12/2019 11:10 PM
"""
import pytest

def add(x, y):
    return x + y

def test_add():
    assert add(1, 0) == 1
    assert add(1, 1) == 2
    assert add(1, 99) == 100




if __name__ == "__main__":
    pytest.main(["-q","test_calc.py"])



