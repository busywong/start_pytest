#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm Community Edition
@file: test_step.py
@time: 2019/4/10 16:44
增量测试的实现  或者说依赖测试的实现
"""


# content of test_step.py

import pytest


@pytest.mark.incremental
class TestUserHandling(object):
    def test_login(self):
        pass

    def test_modification(self):
        assert 0

    def test_deletion(self):
        pass


def test_normal():
    pass

if __name__ == "__main__":
    pytest.main(['-rx','test_step.py'])



