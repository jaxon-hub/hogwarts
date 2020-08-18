"""
__author__ = 'jaxon'
__time__ = '2020/7/8 3:24 下午'
__desc__ = ''
"""
import inspect
import sys

import yaml


def load_yaml(file_path):
    page_name = inspect.stack()[1].function  # 通过栈获取调用者的函数名

    print(load_yaml.__name__)
    with open(file_path, encoding="utf-8") as f:
        yaml_date: dict = yaml.safe_load(f)
    for key,value in yaml_date.items():
        if page_name == key:
            return value

def test_get():
    a = load_yaml("test_data.yaml")
    print(type(a))
    return a
#
if __name__ == '__main__':
    print(test_get())