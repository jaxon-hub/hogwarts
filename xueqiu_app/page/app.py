"""
__author__ = 'jaxon'
__time__ = '2020/6/2 4:13 下午'
"""
import yaml
from appium import webdriver

from xueqiu_app.page.base_page import BasePage
from xueqiu_app.page.main_page import Mainpage


class App(BasePage):
    _appPackage = "com.xueqiu.android"
    _appActivity = ".view.WelcomeActivityAlias"

    def start(self):
        if self._driver is None:
            app_drives = dict()
            app_drives["platformName"] = "Android"
            app_drives["deviceName"] = "hogwarts"
            app_drives["appPackage"] = self._appPackage
            app_drives["appActivity"] = self._appActivity
            # app_drives["noReset"] = "true"
            app_drives["udid"] = yaml.safe_load(open("../page/config.yaml"))["config"]["udid"]

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", app_drives)
        else:
            # self._driver.launch_app() #启动app
            self._driver.start_activity(self._appPackage, self._appActivity) # 如果Activit存在，则启动Activity，不存在则启动app
        # 隐式等待
        self._driver.implicitly_wait(10)
        return self

    def restart(self):
        self._driver.close_app()
        self._driver.launch_app()
        return self

    def close_driver(self):
        self._driver.quit()
        return self

    def main(self) -> Mainpage:
        return Mainpage(self._driver)