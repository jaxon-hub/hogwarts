"""
__author__ = 'jaxon'
__time__ = '2020/5/30 4:00 下午'
"""
from appium.webdriver import webdriver
from appium import webdriver

from hogwarts_app.page.base_page import BasePage
from hogwarts_app.page.main import Main


class App(BasePage):
    # app相关操作
    def start(self):
        if self._driver is None:
            app_drives = {
                "platformName": "Android",
                "deviceName": "192.168.56.102:5555",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                "noReset": "true"
            }
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", app_drives)
            # 隐式等待
            self._driver.implicitly_wait(10)
        else:
            self._driver.launch_app()
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        return Main(self._driver)