# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_10.2_vector_v1
   Description :
   date：          2022/2/17
-------------------------------------------------
"""
import numbers
from array import array
import reprlib
import math


class Vector:
    short_names = 'xyzt'
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __setitem__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.short_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attribute 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise msg
        super().__setattr__(name, value)

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.short_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def len(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    v7 = Vector(range(7))
    print(v7[-1])
    print(v7[1:4])
    print(v7[-1:])
    print(v7[1:2])
