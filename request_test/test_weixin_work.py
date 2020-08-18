"""
__author__ = 'jaxon'
__time__ = '2020/7/3 10:02 上午'
__desc__ = ''
"""
import json
import os
from time import sleep

import pytest
import requests


def test_get_token():
    ID = "ww7647285b6a6484c3"
    corpsecret = "XeNxxhMSKLSJLNHy1YWqrvIIOmLbgwEnw3wUD8UzJSU"
    req = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={ID}&corpsecret={corpsecret}")
    return req.json()['access_token']
    # print(json.dumps(date, sort_keys=True, indent=4, separators=(',', ':')))

def test_create_name():
    date = {
        "name": "广州研发中心",
        "name_en": "RDGZ",
        "parentid": 1,
        "order": 1,
        "id": 2
    }
    req = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={test_get_token()}", json=date)
    print(req.json())
    errmsg = req.json()["errmsg"]
    id = req.json()["id"]
    assert errmsg == "created"
    return id

def test_get_department():
    req = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={test_get_token()}")
    print(req.json())
    errmsg = req.json()["errmsg"]
    id = req.json()["department"][1]["id"]
    assert errmsg == "ok"
    return id

def test_update():
    date = {
        "id": test_get_department(),
        "name": "update",
        "name_en": "update",
        "parentid": 1

    }
    req = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={test_get_token()}",json=date)
    print(date)
    errmsg = req.json()["errmsg"]
    assert errmsg == "updated"
    return None


def test_delete():
    req = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={test_get_token()}&id={test_get_department()}")
    errmsg = req.json()["errmsg"]
    assert errmsg == "deleted"
    return None

if __name__ == '__main__':
    print(test_delete())
    # pytest.main()
