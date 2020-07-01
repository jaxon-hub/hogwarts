"""
__author__ = 'jaxon'
__time__ = '2020/6/2 5:49 下午'
"""
import inspect
import json
import logging

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from xueqiu_app.page.wrapper import handle_black


class BasePage:
    _params = {}
    logging.basicConfig(level=logging.INFO)
    _driver: WebDriver
    _black_list = [

        (MobileBy.ID, "com.xueqiu.android:id/tv_left"),  # 评价弹窗
        (MobileBy.ID, "com.xueqiu.android:id/tv_agree"),  # 同意协议弹窗
    ]
    _max_num = len(_black_list)
    _error_num = 0

    def __init__(self, driver:WebDriver = None):
        self._driver = driver

    def set_implicitly(self, time):
        return self._driver.implicitly_wait(time)

    @handle_black
    def find(self, locator, value:str = None):
        logging.info(f"调用find方法查询元素的方式为：{locator}")
        logging.info(f"调用find方法查询的元素为：{value}")
        elements: WebDriver
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

    @handle_black
    def finds(self, locator, value:str = None):
        logging.info(f"调用finds方法查询元素的方式为：{locator}")
        logging.info(f"调用finds方法查询的元素为：{value}")
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    @handle_black
    def find_text(self, locator, value:str = None):
        if isinstance(locator,tuple):
            element_text = self._driver.find_element(*locator).text
        else:
            element_text = self._driver.find_element(locator, value).text

        return element_text

    def load_yaml(self, file_path):
        page_name = inspect.stack()[1].function     # 通过栈获取调用者的函数名
        with open(file_path, encoding="utf-8") as f:
            yaml_date:dict = yaml.safe_load(f)
        raw = json.dumps(yaml_date)
        for key,value in self._params.items():
            raw = raw.replace("${"+key+"}", value)
        yaml_date = json.loads(raw)
        """↑ 替换name为传进来的参数"""
        """↓ 解析yaml文件"""
        if page_name in yaml_date.keys():
            for date in yaml_date[page_name]:
                logging.info(f"替换后的yaml文件内容为：{yaml_date[page_name]}")
                if "by" in date.keys():
                    element = self.find(date["by"],date["locator"])
                    if date["action"] == "click":
                        element.click()
                    if date["action"] == "send_keys":
                        element.send_keys(date["key"])
                    # if date["action"] == "len > 0":
                    #     eles = self.finds(date["by"],date["locator"])
                    #     return len(eles) > 0
                    if date['action'] == "assert":
                        if element:
                            return True
                        else:
                            return False

    def screen_short(self,name):
        """截图"""
        self._driver.save_screenshot(name)

if __name__ == '__main__':
    a = BasePage()
    params = {"name":"123"}
    filepath = "../page/page.yaml"
    # print(a.load_yaml(filepath,params))
