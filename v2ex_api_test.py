#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm Community Edition
@file: v2ex_api_test.py.py
@time: 2019/4/11 19:48
"""

import requests
import pytest

class TestV2exApi(object):
    domain = 'https://www.v2ex.com/'

    def test_node(self):
        path = 'api/nodes/show.json?name=python'
        url = self.domain + path
        res = requests.get(url).json()
        assert res['id'] == 90
        assert res['name'] == 'python'

    @pytest.fixture(params=['python', 'java'])
    def get_name(self,request):
        return request.param

    def test_node2(self, get_name):
        path = 'api/nodes/show.json?name=%s' % (get_name)
        url = self.domain + path
        res = requests.get(url).json()
        assert res['name'] == get_name
        assert 0   #  使用assert(0)强制用例失败，这样可以看到每次fixture的参数值

    @pytest.mark.parametrize('imput,expect,act',[('3+1',4,'gaga'),('2+4',6,True),('6*9',54,True)])
    def test_eval(self,imput,expect,act):
        print(act)
        assert eval(imput) == expect, act
        assert 0

if __name__ == '__main__':
    pytest.main(['-ra','v2ex_api_test.py::TestV2exApi::test_eval'])