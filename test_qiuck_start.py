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


def str_reverse(string):
    return string[::-1]


def test_str_reverse():
    string = 'good'
    assert str_reverse(string) == 'doog'

    b_string = 'ittest'
    assert str_reverse(b_string) == 'tsetti'

# def main():
#     pass
#
#
# if __name__ == "__main__":
#     main()



