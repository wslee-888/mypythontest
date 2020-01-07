# -*- coding: utf-8 -*-
from typing import Iterable


class Teacher:
    """
以单下划线开头的标识符（如 _width），表示不能直接访问的类属性，其无法通过 from...import* 的方式导入；
以双下划线开头的标识符（如__add）表示类的私有成员；
以双下划线作为开头和结尾的标识符（如 __init__），是专用标识符。
    """

    # name = ""
    # sex = ""
    #
    # __age = 0
    __slots__ = ('love', 'height')

    def __init__(self, *, name, sex, age) -> None:
        self.__age = age
        self.name = name
        self._sex = sex

    # def __new__(cls) -> Any:
    #     return super().__new__(cls)

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)

    def __ne__(self, o: object) -> bool:
        return super().__ne__(o)

    def __str__(self) -> str:
        return "姓名："+self.name+",性别："+self._sex+",年龄："+str(self.__age)

    def __repr__(self) -> str:
        return super().__repr__()

    def __hash__(self) -> int:
        return super().__hash__()

    def __format__(self, format_spec: str) -> str:
        return super().__format__(format_spec)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    def __delattr__(self, name: str) -> None:
        super().__delattr__(name)

    def __sizeof__(self) -> int:
        return super().__sizeof__()

    def __reduce__(self) -> tuple:
        return super().__reduce__()

    def __reduce_ex__(self, protocol: int) -> tuple:
        return super().__reduce_ex__(protocol)

    def __dir__(self) -> Iterable[str]:
        return super().__dir__()

    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
