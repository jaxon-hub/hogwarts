"""
__author__ = 'jaxon'
__time__ = '2020/6/4 5:33 下午'
"""

def ex(fu):
    def hello():
        print("hello")
        fu()
        print("good")
    return hello
@ex
def tmp():
    print("tom")

if __name__ == '__main__':
    # ex(tmp)()
    tmp()