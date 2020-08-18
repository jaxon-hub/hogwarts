"""
__author__ = 'jaxon'
__time__ = '2020/7/5 3:40 下午'
__desc__ = ''
"""
import pytest
import requests


# @pytest.fixture(scope="session")
def test_get_token():
    ID = "ww7647285b6a6484c3"
    corpsecret = "XeNxxhMSKLSJLNHy1YWqrkyp0R6eyVWp5qBIUZSTnc8"
    req = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={ID}&corpsecret={corpsecret}")
    return req.json()['access_token']

def test_create():

    # 创建成员
    date = {
        "userid": '1213',
        "name": "name",
        "mobile": '18300000103',
        "department": [1],
    }
    req = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_get_token()}",
                        json=date)
    print(req.status_code)
    print(req.json())

def test_get():
    # 查询成员
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_get_token()}&userid=123")
    return res.json()

def test_update():
    # 更新成员
    data = {
        "userid": 123,
        "name": "xxx",
        "mobile": 13300000000,
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_get_token()}",
                        json=data)
    return res.json()


def test_delete():
    # 删除成员
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_get_token()}&userid=123")
    return res.json()
