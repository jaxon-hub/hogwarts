"""
__author__ = 'jaxon'
__time__ = '2020/6/2 5:49 下午'
"""
import logging

import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    logging.basicConfig(level=logging.INFO)
    _driver: WebDriver

    def __init__(self, driver:WebDriver = None):
        self._driver = driver

    def find(self, locator, value:str = None):
        logging.info(f"调用find方法查询元素的方式为：{locator}")
        logging.info(f"调用find方法查询的元素为：{value}")
        elements: WebDriver
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)

        return element

    def finds(self, locator, value:str = None):
        _black_list = [

        ]
        logging.info(f"调用finds方法查询元素的方式为：{locator}")
        logging.info(f"调用finds方法查询的元素为：{value}")
        try:
            elements: list
            if isinstance(locator, tuple):
                elements = self._driver.find_elements(*locator)
            else:
                elements = self._driver.find_elements(locator, value)
            return elements
        except:
            for ele in _black_list:
                element = self._driver.find_elements(*ele)
                if len(element) > 0:
                    element[0].click()
                    break
            return self.find(locator, value)

    def find_text(self, locator, value:str = None):

        if isinstance(locator,tuple):
            element_text = self._driver.find_element(*locator).text
        else:
            element_text = self._driver.find_element(locator, value).text

        return element_text

    def load_yaml(self, file_path, page_name):
        try:
            with open(file_path) as f:
                yaml_date = yaml.safe_load(f)
                if page_name in yaml_date.keys():
                    for date in yaml_date[page_name]:
                        if "by" in date.keys():
                            print(date["by"],date["locator"])
                            element = self.find(date["by"],date["locator"])
                            if date["action"] == "click":
                                element.click()
                            if date["action"] == "send_keys":
                                element.send_keys(date["key"])
        except Exception as e:
            logging.info(f"load_yaml方法异常：{e}，文件路径为：{file_path}")
            raise e

if __name__ == '__main__':
    a = BasePage()
    filepath = "page.yaml"
    print(a.load_yaml(filepath,"mainpage"))