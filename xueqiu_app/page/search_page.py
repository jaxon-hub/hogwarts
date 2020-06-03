"""
__author__ = 'jaxon'
__time__ = '2020/6/2 5:34 下午'
"""
from appium.webdriver.common.mobileby import MobileBy

from xueqiu_app.page.base_page import BasePage


class Search(BasePage):

    def search_for_name(self):
        """在搜索页面输入alibba"""
        self.find(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        """点击第二个筛选项"""
        # self.find(MobileBy.XPATH, "//*[@class='androidx.recyclerview.widget.RecyclerView']//.[@class='android.widget.RelativeLayout' and @index='2']").click()
        """点击含有BABA的筛选项"""
        self.find(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/code' and @text='BABA']").click()
        """/..找上一级的父元素；/../..上上级"""
        """点击加自选"""
        self.find(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']/../..//*[@text='加自选']").click()
        return self

    def is_select(self):
        """验证元素（已添加）是否存在（input_name方法内点击的加自选）"""
        select_elements = self.finds(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']/../..//*[@text='已添加']")
        return len(select_elements) > 0
