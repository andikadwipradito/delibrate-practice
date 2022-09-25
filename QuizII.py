from nis import cat
from typing_extensions import Self
from unicodedata import name


class Cat :
    def __init__ (Self, name, age) :
        Self.name = name
        Self.age = age

Cat("Kitty", 3)

print(cat)
