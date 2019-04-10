#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm Community Edition
@file: conftest.py
@time: 2019/4/10 19:14

包/目录级固定装置fixture （设置）,  fixture的作用范围
"""
import pytest


class DB(object):
    pass


@pytest.fixture(scope="session")
def db():
    return DB()


