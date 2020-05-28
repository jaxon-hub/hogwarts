"""
__author__ = 'jaxon'
__time__ = '2020/5/26 5:56 下午'
"""
import time

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


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

    def test_maill(self):
        self.driver.find_element(By.XPATH, "//*[@resource-id='com.tencent.wework:id/ggc']/android.widget.RelativeLayout[2]") .click()
        self.driver.find_element(By.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(By.XPATH, "//*[@text='手动输入添加']").click()
        time.sleep(2)


    def teardown_class(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main()