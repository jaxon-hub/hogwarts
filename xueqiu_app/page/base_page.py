"""
__author__ = 'jaxon'
__time__ = '2020/6/2 5:49 下午'
"""
import logging

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from xueqiu_app.page.wrapper import handle_black


class BasePage:
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

    @handle_black
    def find(self, locator, value:str = None):
        logging.info(f"调用find方法查询元素的方式为：{locator}")
        logging.info(f"调用find方法查询的元素为：{value}")
        elements: WebDriver
        # try:
        #     if isinstance(locator, tuple):
        #         element = self._driver.find_element(*locator)
        #     else:
        #         element = self._driver.find_element(locator, value)
        #     return element
        # except:
        #     for black in  self._black_list:
        #         eleme = self._driver.find_elements(*black)
        #         if len(eleme) > 0:
        #             eleme[0].click()
        #             break
        #     return self.find(locator, value)
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
            # if elements:
            #     return elements
            # else:
            #     raise BaseException
        else:
            elements = self._driver.find_elements(locator, value)
            # if elements:
            #     return elements
            # else:
            #     raise BaseException
        return elements
        # try:
        #     if isinstance(locator, tuple):
        #         element = self._driver.find_elements(*locator)
        #         if element:
        #             return element
        #         else:
        #             raise BaseException
        #     else:
        #         element = self._driver.find_elements(locator, value)
        #         if element:
        #             return element
        #         else:
        #             raise BaseException

            # return element
        # except:
        #     for black in  self._black_list:
        #         eleme = self._driver.find_elements(*black)
        #         logging.info(f"调用finds,---eleme元素为：{eleme}")
        #         if len(eleme) > 0:
        #             eleme[0].click()
        #             break
        #     return self.finds(locator, value)

    def find_text(self, locator, value:str = None):

        if isinstance(locator,tuple):
            element_text = self._driver.find_element(*locator).text
        else:
            element_text = self._driver.find_element(locator, value).text

        return element_text

    # def load_yaml(self, file_path, page_name):
    #     try:
    #         with open(file_path) as f:
    #             yaml_date = yaml.safe_load(f)
    #             if page_name in yaml_date.keys():
    #                 for date in yaml_date[page_name]:
    #                     if "by" in date.keys():
    #                         print(date["by"],date["locator"])
    #                         element = self.find(date["by"],date["locator"])
    #                         if date["action"] == "click":
    #                             element.click()
    #                         if date["action"] == "send_keys":
    #                             element.send_keys(date["key"])
    #     except Exception as e:
    #         logging.info(f"load_yaml方法异常：{e}，文件路径为：{file_path}")
    #         raise e

    def load_yaml(self, file_path):
        try:
            with open(file_path) as f:
                yaml_date = yaml.safe_load(f)
            for date in yaml_date:
                if "action" in date.keys():
                    if date["action"] == "click":
                        print(date["by"], date["locator"])
                        print(date["action"])
                        self.find(date["by"], date["locator"]).click()
        except Exception as e:
            logging.info(f"load_yaml方法异常：{e}，文件路径为：{file_path}")
            raise e


if __name__ == '__main__':
    a = BasePage()
    filepath = "page.yaml"
    print(a.load_yaml(filepath))