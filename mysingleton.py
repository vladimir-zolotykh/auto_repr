#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import weakref


class Singleton(type):
    pass


class Spam(metaclass=Singleton):
    pass


if __name__ == "__main__":
    s1 = Spam()
    s2 = Spam()
    assert s1 is s2
