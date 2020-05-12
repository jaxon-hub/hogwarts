"""
@Time    : 2020/5/9 0009 00:15
@Author  : jaxon
"""
from case.Calc import *
import pytest


class TestCalc:
    def setup(self):
        self.calc = Calc()

    def test_add_one(self):
        result = self.calc.add(1, 2)
        assert 3 == result

    @pytest.mark.run(order=1)
    def test_add_two(self):
        result = self.calc.add(-1, 5)
        assert 4 == result

    def test_add_three(self):
        result = self.calc.add(-1, -2)
        assert -3 == result

    def test_add_four(self):
        result = self.calc.add(-1.11111, -2.2222)
        assert -3.33 == result

    def test_add_five(self):
        result = self.calc.add(0, -2.2222)
        assert -2.22 == result

    def test_add_six(self):
        result = self.calc.add(9999999, 9999999)
        assert 19999998 == result

    def test_add_seven(self):
        result = self.calc.add(-9999999, -9999999)
        assert -19999998 == result

    def test_reduce_one(self):
        result = self.calc.reduce(1, 2)
        assert -1 == result

    def test_reduce_two(self):
        result = self.calc.reduce(-1, 5)
        assert -6 == result

    def test_reduce_three(self):
        result = self.calc.reduce(-1, -2)
        assert 1 == result

    def test_reduce_four(self):
        result = self.calc.reduce(-1.11111, -2.2222)
        assert 1.11 == result

    def test_reduce_five(self):
        result = self.calc.reduce(0, -2.2222)
        assert 2.22 == result

    def test_reduce_six(self):
        result = self.calc.reduce(9999999, 9999999)
        assert 0 == result

    def test_reduce_seven(self):
        result = self.calc.reduce(0, -0)
        assert 0 == result

    def test_multiplication_one(self):
        result = self.calc.multiplication(1, 2)
        assert 2 == result

    def test_multiplication_two(self):
        result = self.calc.multiplication(-1, 5)
        assert -5 == result

    def test_multiplication_three(self):
        result = self.calc.multiplication(-1, -2)
        assert 2 == result

    def test_multiplication_four(self):
        result = self.calc.multiplication(-1.11111, -2.2222)
        assert 2.47 == result

    def test_multiplication_five(self):
        result = self.calc.multiplication(0, -2.2222)
        assert 0 == result

    def test_multiplication_six(self):
        result = self.calc.multiplication(9999999, 9999999)
        assert 99999980000001 == result

    def test_multiplication_seven(self):
        result = self.calc.multiplication(0, -0)
        assert 0 == result

    def test_division_one(self):
        result = self.calc.division(1, 2)
        assert 0.5 == result

    def test_division_two(self):
        result = self.calc.division(-1, 5)
        assert -0.2 == result

    def test_division_three(self):
        result = self.calc.division(-1, -2)
        assert 0.5 == result

    def test_division_four(self):
        result = self.calc.division(-2.2222, -3.33333)
        assert 0.67 == result

    def test_division_five(self):
        result = self.calc.division(0, -2.2222)
        assert 0 == result

    def test_division_six(self):
        result = self.calc.division(9999999, 9999999)
        assert 1 == result

    data_1 = [
        (1, 2, 3),
        (4, 5, 9)
    ]

    # @pytest.mark.parametrize('a, b, expect', data_1)
    @pytest.mark.division
    def test_division_seven(self):
        result = self.calc.division(0, -0)
        assert "分母不能等于0" == result


if __name__ == '__main__':
    # pytest.main()
    # pytest.main(['-vs', 'TestCalc.py::TestCalc::test_division_seven'])
    # 运行spec_001_modul_test模块中用例名称包含seven的用例
    # pytest.main(['TestCalc.py -k " test_division and not two"'])
    pytest.main(['-m', 'division'])
