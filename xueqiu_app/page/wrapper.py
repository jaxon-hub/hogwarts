"""
__author__ = 'jaxon'
__time__ = '2020/6/4 6:46 下午'
"""
from appium.webdriver.common.mobileby import MobileBy


def handle_black(func):
    def handle_windows(*args, **kwargs):
        _black_list = [
            (MobileBy.ID, "com.xueqiu.android:id/tv_agree"), # 同意协议弹窗
            (MobileBy.ID, "com.xueqiu.android:id/tv_left") # 评价弹窗
        ]
        _max_num = len(_black_list)
        _error_num = 0
        from xueqiu_app.page.base_page import BasePage
        instance:BasePage = args[0] # 导入self
        try:
            element = func(*args, **kwargs) #调用穿进来的方法，element为调用目标方法返回的结果
            """如果找到元素则将_error_num设置为0"""
            _error_num = 0
            """恢复隐式等待时间"""
            instance._driver.implicitly_wait(10)
            """如果找到元素，则返回"""
            return element
        except Exception as e:
            """出现异常将隐身等待时间设置小一点，快速处理弹窗"""
            instance._driver.implicitly_wait(2)
            if _error_num > _max_num:
                """判断异常处理次数，如果大于_black_list内元素个数，则抛出异常"""
                _error_num += 1
                raise e
            for ele in _black_list:
                eleme = instance._driver.find_elements(*ele)
                if len(eleme) > 0:
                    eleme[0].click()
                    break
            return instance.find(*args, **kwargs)
    return handle_windows

