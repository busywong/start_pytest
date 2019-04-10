#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm
@file: test_user_password_with_params.py
@time: 4/9/2019 8:32 PM
"""
import pytest
import json

users = json.loads(open('./users.test.json', 'r').read())

class TestUserPasswordWithParam(object):
    @pytest.fixture(params=users)
    def user(self, request):
        return request.param

    def test_user_password(self, user):
        passwd = user['password']
        assert len(passwd) >= 6
        msg = "user %s has a weak password" % (user['name'])
        assert passwd != 'password', msg
        assert passwd != 'password123', msg

if __name__ == "__main__":
    pass



