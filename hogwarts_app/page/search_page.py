"""
__author__ = 'jaxon'
__time__ = '2020/5/31 12:59 上午'
"""
from appium.webdriver.common.mobileby import MobileBy

from hogwarts_app.page.base_page import BasePage


class Search(BasePage):
    def input_name(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/fks").send_keys(self._name)
        return self

    def get_search_resule(self, name):
        search_element = self.find(MobileBy.XPATH, "//*[@text='%s']" % name)
        if not search_element:
            return False
        else:
            return True