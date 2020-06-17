"""
__author__ = 'jaxon'
__time__ = '2020/6/4 6:46 下午'
"""
import logging
import allure
from appium.webdriver.common.mobileby import MobileBy


def handle_black(func):
    logging.basicConfig(level=logging.INFO)
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
            logging.info("run" + func.__name__ + "\n args: \n" +repr(args[1:])+"\n kwargs: \n"+repr(kwargs))
            element = func(*args, **kwargs) #调用传进来的方法，element为调用目标方法返回的结果
            """如果找到元素则将_error_num设置为0"""
            _error_num = 0
            """恢复隐式等待时间"""
            instance._driver.implicitly_wait(5)
            """如果找到元素，则返回"""
            """判断element是否为空，如果不为空则返回，如果为空则抛出异常"""
            if element:
                return element
            else:
                raise Exception
        except Exception as e:
            """发生异常时进行截图,把图片放入allure报告中"""
            instance.screen_short("error.png")
            with open("error.png", "rb") as f:
                content = f.read()
            allure.attach(content,attachment_type=allure.attachment_type.PNG)
            """出现异常将隐身等待时间设置小一点，快速处理弹窗"""
            instance._driver.implicitly_wait(0)
            if _error_num > _max_num:
                """判断异常处理次数，如果大于_black_list内元素个数，则抛出异常"""
                raise e
            _error_num += 1
            for ele in _black_list:
                elelist = instance._driver.find_elements(*ele)
                logging.info(f"处理的黑名单元素为：{ele}")
                if len(elelist) > 0:
                    logging.info(f"处理的黑名单元素为：{elelist[0]}")
                    elelist[0].click()
                    # break
                    return handle_windows(*args, **kwargs)
            raise e
    return handle_windows
