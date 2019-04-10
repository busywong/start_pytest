#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm Community Edition
@file: test_parameter.py
@time: 2019/4/10 14:18
"""
import pytest

@pytest.mark.parametrize('imput,expect',[('3+5',8),('2+4',6),('6*9',42)])
def test_eval(imput,expect):
    assert eval(imput) == expect




if __name__ == "__main__":
    pytest.main(['test_parameter.py'])



