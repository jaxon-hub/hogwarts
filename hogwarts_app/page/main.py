"""
__author__ = 'jaxon'
__time__ = '2020/5/30 4:00 下午'
"""
from appium.webdriver.common.mobileby import MobileBy

from hogwarts_app.page.addresslist_page import AddressList
from hogwarts_app.page.base_page import BasePage


class Main(BasePage):
    # 主页
    def goto_message(self):
        pass

    def goto_mailllist(self):
        self.find(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/ggc']/android.widget.RelativeLayout[2]").click()
        return AddressList(self._driver)

    def goto_workbench(self):
        pass

    def goto_personalcenter(self):
        pass