"""
__author__ = 'jaxon'
__time__ = '2020/6/2 5:49 下午'
"""
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

    def load_yaml(self, file_path, page_name):
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
                    if date["action"] == "len > 0":
                        eles = self.finds(date["by"],date["locator"])
                        return len(eles) > 0
    #
    # def load_yaml(self, path, name):
    #     with open(path, encoding="utf-8") as f:
    #         # name = inspect.stack()[1].function
    #         steps = yaml.safe_load(f)[name]
    #     raw = json.dumps(steps)
    #     for key, value in self._params.items():
    #         raw = raw.replace('${' + key + '}', value)
    #     steps = json.loads(raw)
    #     for step in steps:
    #         if "action" in step.keys():
    #             action = step["action"]
    #             if "click" == action:
    #                 self.find(step["by"], step["locator"]).click()
    #             if "send" == action:
    #                 self.find(step["by"], step["locator"]).send_keys(step["key"])
    #             if "len > 0" == action:
    #                 eles = self.finds(step["by"], step["locator"])
    #                 return len(eles) > 0


def test111(file_path, di, page_name):

    with open(file_path, encoding="utf-8") as f:
        yaml_date: dict = yaml.safe_load(f)
    raw = json.dumps(yaml_date)
    for key, value in di.items():
        print(f"key:{key}")
        raw = raw.replace("${" + key + "}", value)
    yaml_date = json.loads(raw)
    if page_name in yaml_date.keys():
        for date in yaml_date[page_name]:
            # logging.info(f"替换后的yaml文件内容为：{yaml_date[page_name]}")
            if "by" in date.keys():
                print(f'by:{date["by"], date["locator"]}')
    return yaml_date
if __name__ == '__main__':
    a = BasePage()
    params = {"name":"123"}
    filepath = "../page/page.yaml"
    # print(a.load_yaml(filepath,params))
    print(test111(filepath,params,"searchpage"))