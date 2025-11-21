#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import inspect


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
                key_val_pairs = ", ".join(
                    f"{key}={getattr(self, key)!r}" for key in sig.parameters
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


class Circle(metaclass=ReprMeta):
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14 * radius * radius  # Additional attribute not in init


if __name__ == "__main__":
    car = Vehicle("red", 4, 150)
    print(f"Vehicle repr: {repr(car)}")

    circle = Circle(5)
    print(f"Circle repr: {repr(circle)}")
    # Vehicle repr: Vehicle(color='red', wheels=4, speed=150)
    # Circle repr: Circle(radius=5)
