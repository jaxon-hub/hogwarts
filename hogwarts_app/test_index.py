"""
__author__ = 'jaxon'
__time__ = '2020/5/26 5:56 下午'
"""
import time

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from hogwarts_app.CreateDate import ReturnDate


class Testwework:

    def setup_class(self):
        app_drives = {
            "platformName": "Android",
            "deviceName": "192.168.56.102:5555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "noReset": "true"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", app_drives)
        # 隐式等待
        self.driver.implicitly_wait(10)
        self.name = ReturnDate().return_name()
        self.phone = ReturnDate().return_phone()

    def test_maill(self):
        print("添加联系人")
        self.driver.find_element(By.XPATH, "//*[@resource-id='com.tencent.wework:id/ggc']/android.widget.RelativeLayout[2]").click()
        self.driver.find_element(By.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(By.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(By.XPATH, "//*[@text='姓名　']/..//*[@class='android.widget.EditText']").send_keys(self.name)
        self.driver.find_element(By.XPATH, "//*[@text='性别']/..//*[@class='android.widget.ImageView']").click()
        self.driver.find_element(By.XPATH, "//*[@text='女']").click()
        self.driver.find_element(By.XPATH, "//*[@text='手机号']").send_keys(self.phone)
        self.driver.find_element(By.XPATH, "//*[@text='保存后自动发送邀请通知']").click()
        self.driver.find_element(By.ID, "com.tencent.wework:id/gvk").click()
        self.driver.find_element(By.XPATH, "//*[@text='添加成功']")
        time.sleep(2)


    def test_delete_mail(self):
        print("删除联系人")
        self.driver.find_element(By.XPATH,"//*[@resource-id='com.tencent.wework:id/ggc']/android.widget.RelativeLayout[2]").click()
        self.driver.find_element(By.XPATH, "//*[@text='孙斌']").click()
        self.driver.find_element(By.ID, "com.tencent.wework:id/gvd").click()
        self.driver.find_element(By.XPATH, "//android.widget.TextView[@text='编辑成员']").click()
        time.sleep(10)
        self.driver.swipe(547, 1433, 507, 747)
        self.driver.find_element(By.XPATH, "//android.widget.TextView[@text='删除成员']").click()
        # self.driver.find_element(By.ID, "com.tencent.wework:id/b_a").click()

    # def teardown_class(self):
    #     self.driver.quit()

if __name__ == '__main__':
    pytest.main()