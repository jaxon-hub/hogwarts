"""
__author__ = 'jaxon'
__time__ = '2020/5/30 5:20 下午'
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from faker import Faker


class BasePage:
    _balck_list = [
        (MobileBy.XPATH, "//*[@text='确定']"),
        (MobileBy.XPATH, "//*[@text='确认']")
    ]
    _num = 0
    _max_num = 2
    fake = Faker("zh_CN")
    def __init__(self, driver:WebDriver = None):
        self._driver = driver
        self._name = str(self.fake.name())
        self._phone = str(self.fake.phone_number())


    def find(self, locator , value:str = None):
        element:WebDriver
        try:
            if isinstance(locator, tuple):
                # 入参格式：By.XPATH,"//*[@text='添加成员']"
                element = self._driver.find_element(*locator)
            else:
                # 入参格式："//*[@text='添加成员']"
                element = self._driver.find_element(locator,value)
            self._num = 0
            self._driver.implicitly_wait(10)
            return element
        except Exception as e:
            self._driver.implicitly_wait(1)
            if self._num > self._max_num:
                raise e
            self._num +=1
            for ele in self._balck_list:
                balck_element = self._driver.find_elements(*ele)
                if len(balck_element) > 0:
                    balck_element[0].click()
                    return self.find(locator, value)
