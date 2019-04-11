#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm Community Edition
@file: test_sample.py
@time: 2019/4/10 14:46

conftest.py fixture 增加命令选项
"""
import pytest
# content of test_sample.py

cmdopt = 'type1'

def test_answer(cmdopt):
    if cmdopt == "type1":
        print("first")
    elif cmdopt == "type2":
        print("second")
    assert 0  # to see what was printed


if __name__ == "__main__":
    pytest.main(['-q','test_sample.py'])



