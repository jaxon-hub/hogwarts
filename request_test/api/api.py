"""
__author__ = 'jaxon'
__time__ = '2020/7/8 2:41 下午'
__desc__ = ''
"""
from request_test.common.common_api import Common
from request_test.page.base_api import BaseApi


class Api(BaseApi):
    def __init__(self):
        corpid = "ww7647285b6a6484c3"
        corpsecret = "XeNxxhMSKLSJLNHy1YWqrkyp0R6eyVWp5qBIUZSTnc8"
        try:
            self.token = Common().get_token(corpid, corpsecret)
        except Exception as e:
            print(f"Api.__init__ errmsg is :{e.__str__()}")

    def create(self, data_dict):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {
                "access_token": self.token
            },
            "json": data_dict
        }
        return self.send(data)

    def get(self, data_dict):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {
                "access_token": self.token
            }
        }
        data["params"].update(data_dict)
        return self.send(data)

    def update(self, data_dict):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "params": {
                "access_token": self.token
            },
            "json": data_dict
        }
        return self.send(data)

    def delete(self, data_dict):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params": {
                "access_token": self.token
            }
        }
        data["params"].update(data_dict)
        return self.send(data)