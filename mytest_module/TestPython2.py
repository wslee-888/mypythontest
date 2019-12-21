# -*- coding: utf-8 -*-

# import TestImort
import student
import sys
# 自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了sys模块，自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块。
# TestImort.test_import()
# stu = student.Student()
stu = student.Student('老王', 23)
# print(stu.__name)
# stu.get_name_and_score()
# print(student.__author__)
# stu.sex = "男"
# print(stu.sex)
# print(sys.path)
# print(stu._name)
# stu.get_name_and_score()
print(len(stu))
print(str(stu))
print(repr(stu))

arr = [0, 2, 3, 6, 9][0:3]
print(arr)

if isinstance(arr, slice):
    print("arr")


