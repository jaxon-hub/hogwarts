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
            return 'Divisor cannot be 0'


def return_data():
    return [(1, 2, 1), (6, 3, 2)]


def return_F():
    return False

def est():
    for x in range(5):
        yield x     # 生成器： return x+暂停 并且记住了上一步操作的位置


if __name__ == '__main__':
    # print(Calc().add(1, 2))
    # print(Calc().division(2, 0))
    p = est()
    print(next(p))
    print(next(p))
    print(next(p))
