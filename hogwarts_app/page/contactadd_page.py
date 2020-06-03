"""
__author__ = 'jaxon'
__time__ = '2020/5/30 4:17 下午'
"""
from appium.webdriver.common.mobileby import MobileBy

from hogwarts_app.page.base_page import BasePage
from hogwarts_app.page.memberinvite_page import MemberInvite


class ContactAdd(BasePage):
    def input_name(self):
        self.find(MobileBy.XPATH, "//*[@text='姓名　']/..//*[@class='android.widget.EditText']").send_keys(self._name)
        return self

    def select_gender(self):
        self.find(MobileBy.XPATH, "//*[@text='性别']/..//*[@class='android.widget.ImageView']").click()
        self.find(MobileBy.XPATH, "//*[@text='女']").click()
        return self

    def input_phone(self):
        self.find(MobileBy.XPATH, "//*[@text='手机号']").send_keys(self._phone)
        return self

    def no_send_message(self):
        self.find(MobileBy.XPATH, "//*[@text='保存后自动发送邀请通知']").click()
        return self

    def click_save(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/gvk").click()
        return MemberInvite()