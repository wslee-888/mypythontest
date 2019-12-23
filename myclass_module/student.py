# -*- coding: utf-8 -*-

# __author__ = 'li'
# ' a test module '
# __user_name__ = 'liws'


def class_method1():
    pass


class Student(object):
    # __init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
    # 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
    # 特殊方法“__init__”前后分别有两个下划线！！
    # 由于Python是动态语言，根据类创建的实例可以任意绑定属性。
    # 给实例绑定属性的方法是通过实例变量，或者通过self变量：
    name = '老王'

    # def __int__(self):
    #     self.name = '小李'

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name_and_score(self):
        print(self._name, ":", self._score)

    def __len__(self):
        return 21


def class_method2():
    pass
