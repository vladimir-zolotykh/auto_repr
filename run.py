#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import inspect
import logging

logging.basicConfig(level=logging.WARNING)


class ReprMeta(type):
    """
    A metaclass that automatically generates a __repr__ method
    for the class it handles
    """

    def __new__(mcs, name, bases, attrs):
        new_cls = super().__new__(mcs, name, bases, attrs)
        if "__repr__" in attrs:
            return new_cls

        def __repr__(self):
            if "__init__" in attrs:
                sig = inspect.signature(attrs["__init__"])
                logging.info("sig = %s" % sig)
                key_val_pairs = ", ".join(
                    f"{key}={getattr(self, key)!r}"
                    for key in sig.parameters
                    if key != "self"
                )
                return f"{self.__class__.__name__}({key_val_pairs})"
            else:
                key_val_pairs = ", ".join(
                    f"{key}={value!r}" for key, value in self.__dict__.items()
                )
                return f"{self.__class__.__name__}(key_val_pairs)"

        attrs["__repr__"] = __repr__
        return super().__new__(mcs, name, bases, attrs)


class Vehicle(metaclass=ReprMeta):
    def __init__(self, color, wheels, speed):
        self.color = color
        self.wheels = wheels
        self.speed = speed


def run_test():
    """

    >>> car = Vehicle("red", 4, 150)
    >>> car
    Vehicle(color='red', wheels=4, speed=150)
    >>> circle = Circle(5)
    >>> circle
    Circle(radius=5)

    """
    import doctest

    doctest.testmod()


class Circle(metaclass=ReprMeta):
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14 * radius * radius  # Additional attribute not in init


if __name__ == "__main__":
    run_test()
