"""
@Time    : 2020/5/18 0018 22:26
@Author  : jaxon
"""

#
# class Person:
#
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print(f"{self.name} is eating")
#
#
# p = Person('json')
# print(hasattr(p, 'name'))   # 判断实例有没有此属性或者方法
# print(getattr(p, 'name'))   # 获取属性值


def li(list_old):
    for x in range(len(list_old)-1,0,-1):
        print("x",x)
        for y in range(0,x):
            # print("y",y)
            if list_old[y] > list_old[y+1]:
                list_old[y], list_old[y+1] = list_old[y+1],list_old[y]
    return list_old


if __name__ == '__main__':
    a = [3,6,99,11,1,2,4,0]
    print(li(a))
