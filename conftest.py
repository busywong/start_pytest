#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm Community Edition
@file: conftest.py
@time: 2019/4/10 15:04
"""


import pytest

#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
#     )
# @pytest.fixture
# def cmdopt(request):
#     return request.config.getoption("--cmdopt")

#
# def pytest_report_header(config):   # 向测试报告头添加信息
# #     return "project deps: mylib-1.1"

def pytest_report_header(config):
    if config.getoption("verbose") > 0:
        return ["info1: did you know that ...", "did you?"]

# content of conftest.py

import pytest

#根据命令行选项控制跳过测试
# def pytest_addoption(parser):
#     parser.addoption(
#         "--runslow", action="store_true", default=False, help="run slow tests"
#     )
# def pytest_collection_modifyitems(config, items):
#     if config.getoption("--runslow"):
#         # --runslow given in cli: do not skip slow tests
#         return
#     skip_slow = pytest.mark.skip(reason="need --runslow option to run")
#     for item in items:
#         if "slow" in item.keywords:
#             item.add_marker(skip_slow)

# content of conftest.py

#  实现增量测试

# def pytest_runtest_makereport(item, call):
#     if "incremental" in item.keywords:
#         if call.excinfo is not None:
#             parent = item.parent
#             parent._previousfailed = item
#
#
# def pytest_runtest_setup(item):
#     if "incremental" in item.keywords:
#         previousfailed = getattr(item.parent, "_previousfailed", None)
#         if previousfailed is not None:
#             pytest.xfail("previous test failed (%s)" % previousfailed.name)

# content of conftest.py

import pytest
import os.path

# 实现后置处理
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    # print('item is  %s \n' % item)
    outcome = yield
    rep = outcome.get_result()

    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"

        with open(os.path.dirname(__file__)+"\\failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""

            f.write(rep.nodeid + extra + "\n")

if __name__ == "__main__":
    pass



