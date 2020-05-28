"""
@Time    : 2020/5/15 0015 23:18
@Author  : jaxon
"""

from case.Calc import *
import pytest


class Logincase:
    def setup(self):
        self.calc = Calc()

    def case_add_one(self):
        result = self.calc.add(1, 2)
        assert 3 == result

    @pytest.mark.run(order=1)
    def case_add_two(self):
        result = self.calc.add(-1, 5)
        assert 4 == result

    def add_two(self):
        result = self.calc.add(-1, 6)
        assert 4 == result


if __name__ == '__main__':
    pytest.main()