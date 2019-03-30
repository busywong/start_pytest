#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm
@file: test_qiuck_start.py
@time: 3/12/2019 11:04 PM
"""

#!/usr/bin/python
# coding:utf-8
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm
@file: test_qiuck_start.py
@time: 3/12/2019 10:54 PM
"""
import pytest


def str_reverse(string):
    return string[::-1]


def test_str_reverse():
    string = 'good'
    assert str_reverse(string) == 'doog'

    b_string = 'ittest'
    assert str_reverse(b_string) == 'tsetti'

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
def test_zero_division():
    with pytest.raises(ZeroDivisionError):  # ZeroDivisionError
        1 / 0
@pytest.mark.xfail(raises=AssertionError)  #AssertionError
def test_f():
    pass

if __name__ == '__main__':
    pytest.main(["-ra","test_quick_start.py"])

# def main():
#     pass
#
#
# if __name__ == "__main__":
#     main()



