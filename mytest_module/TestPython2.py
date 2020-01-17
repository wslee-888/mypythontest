# -*- coding: utf-8 -*-

# import TestImort
# import student
import sys
# 自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了sys模块，自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块。
# TestImort.test_import()
# stu = student.Student()
# stu = student.Student('老王', 23)
# print(stu.__name)
# stu.get_name_and_score()
# print(student.__author__)
# stu.sex = "男"
# print(stu.sex)
# print(sys.path)
# print(stu._name)
# stu.get_name_and_score()
# print(len(stu))
# print(str(stu))
# print(repr(stu))
#
# arr = [0, 2, 3, 6, 9][0:3]
# print(arr)
#
# if isinstance(arr, slice):
#     print("arr")

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'F://Tesseract-OCR//tesseract.exe'
tessdata_dir_config = r'--tessdata-dir "F://Tesseract-OCR//tessdata" --psm 6'
image = Image.open(r"C:\Users\fcz01\Desktop\图片\购物袋图片\yichen_dai@2x.png")
code = pytesseract.image_to_string(image, lang='chi_sim+eng', config=tessdata_dir_config)
print(code)
