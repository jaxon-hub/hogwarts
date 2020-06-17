"""
__author__ = 'jaxon'
__time__ = '2020/6/2 5:18 下午'
"""
from appium.webdriver.common.mobileby import MobileBy

from xueqiu_app.page.base_page import BasePage
from xueqiu_app.page.market_page import Market


class Mainpage(BasePage):

    def main_activity(self):
        """雪球app主页"""
        return self

    def goto_market(self):
        """主页--行情"""
        self.set_implicitly(10)
        self.load_yaml("../page/page.yaml")
        self.set_implicitly(3)
        return Market(self._driver)