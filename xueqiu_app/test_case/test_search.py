"""
__author__ = 'jaxon'
__time__ = '2020/6/2 7:11 下午'
"""
import pytest
import yaml

from xueqiu_app.page.app import App


class Test_case:
    def setup(self):
        self.app = App()
        self.search = App().start().main().goto_market().goto_search()

    @pytest.mark.parametrize("name",yaml.safe_load(open("../test_case/test_search.yaml", encoding="utf-8")))
    def test_search(self, name):
        self.search.search_for_name(name)
        self.search.add(name)
        assert self.search.is_select(name)
        self.search.reset(name)


    # def teardown_class(self):
    #     self.app.close_driver()
    #
    # @pytest.mark.parametrize("value, value1", yaml.safe_load(open("../page/test_date.yaml")))
    # def test_date_config(self, value, value1):
    #     print(value)
    #     print(value1)
