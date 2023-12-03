# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 17:19
# @Author  : Zeeland
# @File    : demo4_class.py
# @Software: PyCharm

import logging

from broadcast_service import broadcast_service

logging.basicConfig(level=logging.DEBUG)


class Component:
    def __init__(self):
        pass

    @broadcast_service.on_listen("activate component")
    def handle_callback(self, value):
        print(self)
        print(value)

    def method(self):
        broadcast_service.broadcast("activate component", self, "ohohohohoh")


if __name__ == "__main__":
    c1 = Component()
    c1.method()
