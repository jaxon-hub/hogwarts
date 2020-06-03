"""
__author__ = 'jaxon'
__time__ = '2020/6/2 7:11 下午'
"""
import pytest
import yaml

from xueqiu_app.page.app import App


class Test_case:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().main()

    def test_search(self):
        search_re = self.main.goto_market().goto_search()
        assert search_re.search_for_name().is_select()


    @pytest.mark.parametrize("value, value1", yaml.safe_load(open("../page/test_date.yaml")))
    def test_date_config(self, value, value1):
        print(value)
        print(value1)
