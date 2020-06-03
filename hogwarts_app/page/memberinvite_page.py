"""
__author__ = 'jaxon'
__time__ = '2020/5/30 4:13 下午'
"""
from appium.webdriver.common.mobileby import MobileBy

from hogwarts_app.page.addresslist_page import AddressList
from hogwarts_app.page.base_page import BasePage


class MemberInvite(BasePage):
    # 添加成员-手动添加
    def member_by_addmenually(self):
        from hogwarts_app.page.contactadd_page import ContactAdd
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return ContactAdd(self._driver)

    def get_tost(self):
        return self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text()

    # def goto_return(self):
    #     self.find(MobileBy.ID, "com.tencent.wework:id/gv3").click()
    #     return AddressList(self._driver)