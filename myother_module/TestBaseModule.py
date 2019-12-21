# 导入turtle包的所有内容:
# from turtle import *
from functools import reduce
import functools
import turtle


def hua_tu():
    my_turtle = turtle.Turtle()
    # 设置笔刷宽度:
    my_turtle.width(4)
    # 前进:
    my_turtle.forward(200)
    # 右转90度:
    my_turtle.right(90)
    # 笔刷颜色:
    my_turtle.pencolor('red')
    my_turtle.forward(200)
    my_turtle.right(90)

    my_turtle.pencolor('green')
    my_turtle.forward(200)
    my_turtle.right(90)

    my_turtle.pencolor('blue')
    my_turtle.forward(200)
    my_turtle.right(90)
    # 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
    # my_turtle.done();


def my_method(x, y):
    if x > y:
        print("x 大于 y")
    elif x < y:
        print("x 小于 y")
    else:
        print("x 等于 y")
    # return
    # return None


def di_gui(n):
    if n == 1:
        return 1
    return n * di_gui(n-1)


# 实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
def non():
    pass


# 返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple
def move_on_game(x, y):
    return x, y


# 默认参数
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错
# 二是如何设置默认参数。
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def default_method(x, y, n=2):
    print("y的值：", y)
    return pow(x, n)


def add_end(l1=[]):
    l1.append('END')
    return l1


def add_end(l1=None):
    l1.append('END')
    return l1


# 可变参数,参数接收到的是一个tuple
def calc(*num):
    sum1 = 0
    for n in num:
        sum1 = sum1 + n * n
    return sum1


# 关键字参数,而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict,可以只传入必选参数,也可以传入任意个数的关键字参数：
def key_method(name, age, **key):
    print('必填参数1:', name, '必填参数2:',  age, key)


# 命名关键字参数,如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数,关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def key_method_on_name(name, age, *, city, job):
    print(name, age, city, job)


# 命名关键字参数可以有缺省值
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, args, city, job)


# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'

# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


def add_abs(x, y, myabs):
    return myabs(x) + myabs(y)


def f(x):
    return x * x


def r(x, y):
    return x + y


# python支持函数式编程，但是函数基本性质和作用域不变
# def test1(x, y):
#     def test2(z):
#         y = y + 100
#     test2(13)
#     print(x)
#     print(y)
#
#


def test3(x, y):
    def test5():
        # print("test53的x值：", x)
        # z = x + 50
        # print(z)
        # print("test5的z值：", z)
        # x = y - 100
        x = 100
        z = x - 100
        print(x)
        # x = 100
        # print("test5的x值：", x)
    test5()
    print("test3的x值：", x)
    print("test3的y值：", y)


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))


def test6(x):
    if x % 2 == 0:
        return False
    else:
        return True


def _odd_iter():
    n = 1
    while True:
        n = n+2
    yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    # 初始序列
    it = _odd_iter()

    while True:
        # 返回序列的第一个数
        n = next(it)
        yield n
        # 构造新序列
        it = filter(_not_divisible(n), it)


# 我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


def test7():
    x = 200

    def test8():
        x = 100
        return x
    return test8


def log1(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


def log3(text2):
    def decorator2():
        def decorator1(func):
            def wrapper(*args, **kw):
                print('%s %s():' % (text2, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator1
    return decorator2


def log5(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log6(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log6('test2')
def now():
    return '2019-04-10 00:00:00'

