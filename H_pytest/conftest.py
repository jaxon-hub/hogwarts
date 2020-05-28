"""
@Time    : 2020/5/14 0014 23:50
@Author  : jaxon
"""
import pytest


def pytest_collection_modifyitems(session, config, items: list):
    # print(items)
    # print(type(items))
    # for item in items:
    #     if 'one' in item.nodeid:
    #         item.add_marker(pytest.mark.one)
    #     elif 'two' in item.nodeid:
    #         item.add_marker(pytest.mark.two)
    items.reverse()