"""
__author__ = 'jaxon'
__time__ = '2020/6/2 5:34 下午'
"""
from appium.webdriver.common.mobileby import MobileBy

from xueqiu_app.page.base_page import BasePage


class Search(BasePage):

    def search_for_name(self, name):
        """在搜索页面输入alibba"""
        self._params["name"] = name
        self.load_yaml("../page/page.yaml")

    def add(self, name):
        """点击加自选"""
        self._params["name"] = name
        self.load_yaml("../page/page.yaml")

    def is_select(self, name):
        self._params["name"] = name
        """验证元素（已添加）是否存在（add方法内点击的加自选）"""
        return self.load_yaml("../page/page.yaml")

    def reset(self, name):
        """取消自选"""
        self._params["name"] = name
        return self.load_yaml("../page/page.yaml")

