"""
__author__ = 'jaxon'
__time__ = '2020/5/30 4:39 下午'
"""
import pytest

from hogwarts_app.page.app import App
from hogwarts_app.page.base_page import BasePage
from hogwarts_app.page.search_page import Search


class TestRun:
    def setup_class(self):
        self.app = App()
        # 启动app进入首页
        self.main = self.app.start().main()

    def test_case(self):
        # 首页--通讯录--添加成功--手动添加--输入信息--点击保存
        resule_page = self.main.goto_mailllist().add_memder().member_by_addmenually().\
            input_name().select_gender().input_phone().no_send_message().click_save().goto_return()
        # assert '添加成功' in result_page.get_tost()


if __name__ == '__main__':
    pytest.main()