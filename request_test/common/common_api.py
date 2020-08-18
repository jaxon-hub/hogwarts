"""
__author__ = 'jaxon'
__time__ = '2020/7/8 2:35 下午'
__desc__ = ''
"""
import inspect
import json
import logging
import yaml
from request_test.page.base_api import BaseApi


class Common(BaseApi):
    _params = {}
    logging.basicConfig(level=logging.INFO)
    def get_token(self, corpid, corpsecret):
        print("get_token")
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }
        return self.send(data)["access_token"]

    def load_yaml(self,file_path):
        method_name = inspect.stack()[1].function  # 通过栈获取调用者的函数名
        with open(file_path, encoding="utf-8") as f:
            yaml_date: dict = yaml.safe_load(f)
        raw = json.dumps(yaml_date)
        for key, value in self._params.items():
            raw = raw.replace("${" + key + "}", value)
        yaml_date = json.loads(raw)
        """↑ 替换name为传进来的参数"""
        """↓ 解析yaml文件"""
        for key, value in yaml_date.items():
            if method_name == key:
                return value
