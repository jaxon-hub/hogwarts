"""
__author__ = 'jaxon'
__time__ = '2020/6/4 6:46 下午'
"""
import logging

from appium.webdriver.common.mobileby import MobileBy


def handle_black(func):
    def handle_windows(*args, **kwargs):
        logging.basicConfig(level=logging.INFO)
        _black_list = [

            (MobileBy.ID, "com.xueqiu.android:id/tv_left"), # 评价弹窗
            (MobileBy.ID, "com.xueqiu.android:id/tv_agree"), # 同意协议弹窗
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
            instance._driver.implicitly_wait(5)
            """如果找到元素，则返回"""
            logging.info(f"element：{element}")
            """判断element是否为空，如果不为空则返回，如果为空则抛出异常"""
            if element:
                return element
            else:
                raise Exception
        except Exception as e:
            """出现异常将隐身等待时间设置小一点，快速处理弹窗"""
            instance._driver.implicitly_wait(0)
            if _error_num > _max_num:
                """判断异常处理次数，如果大于_black_list内元素个数，则抛出异常"""
                raise e
            _error_num += 1
            for ele in _black_list:
                elelist = instance._driver.find_elements(*ele)
                logging.info(f"elelist为：{elelist}")
                logging.info(f"ele：{ele}")
                if len(elelist) > 0:
                    logging.info(f"处理的黑名单元素为：{elelist[0]}")
                    elelist[0].click()
                    # break
                    return handle_windows(*args, **kwargs)
        raise e
    return handle_windows
