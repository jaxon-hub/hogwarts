"""
__author__ = 'jaxon'
__time__ = '2020/5/30 4:08 下午'
"""
from appium.webdriver.common.mobileby import MobileBy

from hogwarts_app.page.base_page import BasePage


class AddressList(BasePage):
    #通讯录-添加成员页面
    def add_memder(self):
        from hogwarts_app.page.memberinvite_page import MemberInvite
        self.find(MobileBy.XPATH, "//*[@text='添加成员']").click()
        return MemberInvite(self._driver)

    # def search_name(self):
    #     self.find(MobileBy.ID,"com.tencent.wework:id/gvn").click()
    #     from hogwarts_app.page.search_page import Search
    #     return Search(self._driver)