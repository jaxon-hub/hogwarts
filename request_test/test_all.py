"""
__author__ = 'jaxon'
__time__ = '2020/7/8 3:18 下午'
__desc__ = ''
"""
import allure

from request_test.api.api import Api
from request_test.common.common_api import Common

@allure.epic("11111")
class TestApi():
    def setup(self):
        self.api = Api()
        self.common = Common()

    @allure.story("story")
    @allure.description("description")
    @allure.issue("issue")
    @allure.title("title")
    def test_create(self):
        self.common._params["userid"] = "66666"
        self.common._params["name"] = "wangmazi"
        self.common._params["mobile"] = "18898887888"
        re = self.api.create(self.common.load_yaml("./test_data.yaml"))
        print(re)

    def test_get(self):
        self.common._params["userid"] = "3344"
        re = self.api.get(self.common.load_yaml("./test_data.yaml"))
        print(re)

    def test_update(self):
        self.common._params["userid"] = "3344"
        self.common._params["name"] = "zhangsann"
        self.common._params["mobile"] = "18888887888"
        re = self.api.update(self.common.load_yaml("./test_data.yaml"))
        print(re)

    @allure.story("story222")
    def test_delete(self):
        self.common._params["userid"] = "3344"
        re = self.api.delete(self.common.load_yaml("./test_data.yaml"))
        print(re)

        # pytest -test_xxx.py(测试脚本) --alluredir=./result