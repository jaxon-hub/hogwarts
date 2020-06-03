"""
__author__ = 'jaxon'
__time__ = '2020/5/30 2:20 下午'
"""
from faker import Faker


fake = Faker("zh_CN")


class ReturnDate:

    def return_name(self):
        return str(fake.name())

    def return_phone(self):
        return str(fake.phone_number())

if __name__ == '__main__':
    print(ReturnDate().return_phone())
