#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import weakref
import logging

logging.basicConfig(level=logging.DEBUG)


class Singleton(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        logging.info("cls.__name__ = %s" % cls.__name__)
        if not cls._instance:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Spam(metaclass=Singleton):
    pass


class Conn(metaclass=Singleton):
    pass


if __name__ == "__main__":
    s1 = Spam()
    s2 = Spam()
    c = Conn()
    print("s1 is s2 = ", s1 is s2)
    print("c is s1 = ", c is s1)
