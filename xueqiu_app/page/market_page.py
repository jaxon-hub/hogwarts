"""
__author__ = 'jaxon'
__time__ = '2020/6/3 1:35 上午'
"""
from appium.webdriver.common.mobileby import MobileBy

from xueqiu_app.page.base_page import BasePage
from xueqiu_app.page.search_page import Search


class Market(BasePage):
    def goto_search(self):
        self.find(MobileBy.ID, "com.xueqiu.android:id/action_search").click()
        # self.load_yaml("../page/page.yaml","marketpage")
        return Search(self._driver)