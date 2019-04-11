#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm
@file: test_parameterized.py
@time: 4/9/2019 8:46 PM
"""
import pytest


@pytest.mark.parametrize('imput,expect',[('3+5',8),('2+4',6),('6*9',42)])
def test_eval(imput,expect):
    assert eval(imput) == expect


if __name__ == "__main__":
    pytest.main(['test_parameterized.py'])



