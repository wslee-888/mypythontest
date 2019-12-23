# -*- coding: utf-8 -*-

# a = 100;
# b = 200;
#
# c = '学习python';
#
# print('a + b =',a+b);

# print(not False)
#
# print(10/3)
# print(10//3)
# print(10%3)
#
# print(10*56)

# print(ord('X'))
#
# print(chr(88))


# print('%2d-%02d' % (3, 1))
# print('%.2f' % 3.1415926)

# print('''1
# 23
# 45
# 6
# 7
# 89''')

# print('亲爱的%s你好！你%d月的话费是%3f元，余额是%2f元' % ('隔壁老王',2,56.23,23.68))

# print('请输入你的名字');
# name = input();

# print('你好，',name);


# named = True and False;
# print(d);
#
#
# e = c;
# f = 300;
# f = f + b;
#
# print(e);
#
# print(f);
#
# print('学习python');
#
# g = len('学习python');
#
# print(g);
# print('c'+'asf')
# arr = []和arr2 = ('一号','二号','三号')相当于java的list集合

# arr = []
# print(arr)
#
# len = len(arr);
# print('数组长度：',len);
# arr.append('感觉坏坏的')
# arr.append('你妹的')
# print(arr)
# arr.insert(2,"java")
# print(arr)
#
# arr.pop()
# print(arr)
#
# arr.pop(2)
# print(arr)

# 二维甚至多维数组
# s = ['python', 'java', ['asp', 'php'], 'scheme']

# for str in arr:
#     print(str);
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
# arr2 = ('一号','二号','三号')
# for arr2str in arr2:
#  print(arr2str);
# print(arr2[0])
# print(arr2[len(arr2)-1])
# print(arr2[-1])
# print(arr2[-len(arr2)])
# print(('一号', '二号', '三号')[1:])
# arr2 = ()
# arr2 = (1)
# print(arr2)
# arr2 = (10,)
# print(arr2)

# 切片不包括结束索引号对应的元素,如果第一个索引是0，还可以省略
# print(s[1:3])
# print(s[1:])
# print(s[:])
# print(s[:2])
# 倒切片
# print(s[-4:])
# print(s[:-2])
# L = list(range(100))
# print(L[10:30:3])

# print((0, 1, 2, 3, 4, 5)[:3])
# print('ABCDEFG'[:3])


# t = ('a', 'b', ['A', 'B'])
#
# if n > 0:
#     print("n大于零")
# elif n == 0:
#     print("n等于零")
# else:
#     print

# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
# x = 100;
# if x:
#     print('True')
# 代码块缩进4格，最好不要空行太多，
# 数组元素需要空格隔开
# myList = [0, 2, 6, 9, 10]

#
# for i in range(5):
#     print("myList第",i,"个元素:",myList[i])
#
# for j in myList:
#     print(j)
#     if j <= 6:
#         continue
#     else:
#         break


# 使用dict和set，相当于java的map集合
# 注意编写的规范
# pythonMap = {'一号': 1, '二号': 2, '三号': 3}
# print(pythonMap['一号'])
# for key in pythonMap.keys():
#     print('key:', key, ':', 'value:', pythonMap.get(key))

# for key, value in pythonMap:
#     print("key:", key, "value:", value)

# for key, value in pythonMap.items():
#     print("key:", key, "value:", value)
#
# for value in pythonMap.values():
#     print("value:", value)


# pythonMap.pop('二号')
# print(pythonMap)

# for item in pythonMap.items():
#     print(item.key)
# print(pythonMap.items())

# s = set([11, 23, 66, 11, 23])
# print(s)
#
# s.add('acv')
# print(s)
#
# s.remove('acv')
# print(s)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
# s1 = set([11, 23, 66])
# s2 = set([22, 23, 55])
# print(s1 & s2)
# str = "abnchdfkf"
# for ch in str:
#     print(ch)

# 判断当前数据类型是否可以迭代
# from collections.abc import Iterable
# print(isinstance('absnsdhd', Iterable))
# print(isinstance([12, 23, 69], Iterable))

# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)
#
# for x in [(1, 1, 3), (2, 4, 6), (3, 9, 9)]:
#     print(x)

# 有点像双层循环
# for x, y, z in [(1, 1, 3), (2, 4, 6), (3, 9, 9)]:
#     print(x, y, z)

# 列表生成式
# print([x * x for x in range(1, 11)])
# print([x/10 for x in range(2, 20) if x % 2 == 0])
# print([m+n+v for m in 'abc' for n in 'def' for v in 'xyz'])
# import os
# print([dir for dir in os.listdir('C:\\Users\\fcz01\\Desktop\\dbdata')])
#
# print([str for str in 'asfdaasfaf'])
# 循环其实可以同时使用两个甚至多个变量,因此，列表生成式也可以使用两个变量来生成list
# d = {'x': 'A', 'y': 'B', 'z': 'C'}
# print([k + '=' + v for k, v in d.items()])
#
# L = ['Hello', 'World', 'IBM', 'Apple']
# print([s.lower() for s in L])

# print(isinstance(123, int))
# print(isinstance('abc', str))
# print(isinstance(1.23, float))
# print(isinstance(True, bool))

# 生成器,一边循环一边计算的机制，称为生成器：generator
# g = (x * x for x in range(10))
# next(g)
# for x in g:
#     print(x)
# a, b = 1, 2
# print('a的值：', a, 'b的值：', b)
# b, b = b, a
# print('a的值：', a, 'b的值：', b)

# 查看更多python方法，https://docs.python.org/3/library/functions.html
# help(abs)
# y = 200
# s = 'add'
# print(int(y))
# 注意方法编写的规范
# def _my_method_(i):
#     if i > 0:
#         return '大于零'
#     elif i == 0:
#         return '等于零'
#     else:
#         return '小于零'
#
#
# print(_my_method_(0))
# import TestBaseModule
# TestBaseModule.hua_tu()
# TestBaseModule.my_method(20, 20)
# print("10的递归结果：",TestBaseModule.di_gui(10))
# import TestBaseModule
# from TestBaseModule import hua_tu
# hua_tu()
# print(TestBaseModule.di_gui(10))
# print(TestBaseModule.my_method(10, 23))
# print(TestBaseModule.non())
# print(TestBaseModule.move_on_game(100, 200))
# print(TestBaseModule.default_method(100, 200))
# print(TestBaseModule.default_method(100, 200, 3))

# arr3 = [1, 2, 3]
# print(TestBaseModule.calc(1, 2, 3))
# print(TestBaseModule.calc(*arr3))

# dic3 = {'王大锤': '白客', '暴走大事件': '王大锤'}
# print(TestBaseModule.key_method('王大锤', 28))
# print(TestBaseModule.key_method('王大锤', 28, num = 12, str = '好的'))
# print(TestBaseModule.key_method('Jack', 24, 王大锤=dic3['王大锤'], 暴走大事件=dic3['暴走大事件']))
# print(TestBaseModule.key_method('王大锤', 28, **dic3))

# TestBaseModule.key_method_on_name('王尼玛', 28, city='深圳', job='暴走大事件主持人')
# f = TestBaseModule.fib(10)
# print(f)

# try:
#     for x in f:
#         print(x)
# except StopIteration as e:
#     print(e.value)

# while True:
#     try:
#         x = next(f)
#         print(x)
#     except StopIteration as e:
#         print(e.value)
#         break

# 因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算
# from collections.abc import Iterator
#
# print(isinstance((x for x in range(10)), Iterator))
#
# print(isinstance([], Iterator))
#
# print(isinstance({}, Iterator))
#
# print(isinstance('abc', Iterator))
#
# print(isinstance(iter([]), Iterator))

# 变量可以指向函数
# myabs = abs
# print(myabs(-33.69))

# abs = 10
# print(abs(-10))
# 函数名也是变量,把abs指向10后，就无法通过abs(-10)调用该函数了！因为abs这个变量已经不指向求绝对值函数而是指向一个整数10！

# 传入函数
# print(TestBaseModule.add_abs(-10, -20, myabs))

# 高阶函数实例1：map和reduce

# map返回的是迭代器
# from TestBaseModule import f
# it = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(list(it))
#
# it = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(list(it))

import TestBaseModule
# from functools import reduce
import functools
# from collections.abc import Iterator
# from collections.abc import Iterable
#
# itOrList = TestBaseModule.fib(6)
#
# print(itOrList)
# print(isinstance(itOrList, Iterable))
# print(isinstance(itOrList, Iterator))


# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# it = reduce(r, [1, 2, 3, 4, 5])
# print(it)
# TestBaseModule.test1(10, 200)
# TestBaseModule.test2()

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# newarr = filter(TestBaseModule.test6, arr)
# print(list(newarr))

# print(TestBaseModule.str2int("12589"))

# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。对比原始的list和经过key=abs处理过的list：
# arr = [1, -12, -23, 33]
# arr2 = sorted(arr)
# print(arr)
# print(arr2)
#
#
# arr3 = sorted(arr, key=abs, reverse=True)
# print(arr3)

# test = TestBaseModule.test7()
# print(test)
# print(test())


# 匿名函数
# f = lambda x: x + 100
# print(f(100))

# f = TestBaseModule.now
# print(f.__name__)
#
# print(TestBaseModule.now())
# print(int('0111101', base=2))

# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
# 实际上可以接收函数对象、*args和**kw这3个参数，当传入
# int2 = functools.partial(int, base=2)
# print(int2("01110"))
# print(int2("1234689", base=10))
#
# max2 = functools.partial(max, 10)


a = 1
b = 2

# 这种赋值计算，先计算右边，再把结果相应地赋值给左边
a, b = b, a + b
print(a)
print(b)

c = 5
d = 6

c, d = d, c
print(c)
print(d)


