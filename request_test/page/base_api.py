"""
__author__ = 'jaxon'
__time__ = '2020/7/8 2:11 下午'
__desc__ = ''
"""
import logging

import requests


class BaseApi:

    def send(self, data):
        logging.basicConfig(level=logging.INFO)
        # return requests.request(**data).json()
        try:
            req = requests.request(**data)
            req_code = req.status_code
            if req_code == 200:
                logging.info(f"Response为200，返回内容为{req.json()}")
                return req.json()
            if req_code != 200:
                logging.info(f"Response为:{req_code}，返回内容为{req.text}")
                return req.text
        except Exception as e:
            return f"send errmsg is : {e.__str__()}"


if __name__ == '__main__':
    pass
