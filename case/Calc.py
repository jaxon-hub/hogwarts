"""
@Time    : 2020/5/8 22:49
@Author  : jaxon
"""


class Calc:

    def add(self, a: float, b: float) -> float:
        """
        :param a: float
        :param b: float
        :return: a + b
        """
        result = a + b
        return round(result, 2)

    def reduce(self, a: float, b: float) -> float:
        """
        :param a: float
        :param b: float
        :return: a -b
        """
        result = a - b
        return round(result, 2)

    def multiplication(self, a: float, b: float) -> float:
        """
        :param a: float
        :param b: float
        :return: a*b
        """
        result = a * b
        return round(result, 2)

    def division(self, a: float, b: float) -> float:
        """
        :param a: float
        :param b: float
        :return: a/b
        """
        try:
            result = a/b
            return round(result, 2)
        except:
            return '分母不能等于0'


if __name__ == '__main__':
    print(Calc().add(1, 2))
    print(Calc().division(2, 0))

