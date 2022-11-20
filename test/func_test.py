# -*- coding: utf-8 -*-
# @Time    : 2022/11/20 09:24
# @Author  : Zeeland
# @File    : func_test.py
# @Software: PyCharm

from broadcast_service import broadcast_service
import time

position = ['home', 'company']

class Leader:
    def __init__(self, name):
        self.current_position = position[1]
        self.name = name

    def notice_meeting(self):
        print('[leader] {0} notice meeting now.'.format(self.name))
        meeting_info = 'our company will go bankrupt soon'
        broadcast_service.broadcast('meeting', meeting_info)

class Staff:
    def __init__(self, name):
        self.current_position = position[0]
        self.name = name
        self.rec_msg()

    def rec_msg(self):
        broadcast_service.listen('meeting', self.go_meeting)

    def go_meeting(self, info):
        if self.current_position == position[0]:
            self.current_position = position[1]
        print('[staff] {0} go meeting now.'.format(self.name))
        time.sleep(1)
        print('[staff] {0} rec msg: {1}'.format(self.name, info))

class FuncTest:
    def run(self):
        self.init_test()
        self.go_meeting_test()

    def init_test(self):
        self.leader = Leader('Tom')
        self.staff1 = Staff('Jack')
        self.staff2 = Staff('Jasmine')
        self.staff3 = Staff('Jane')

    def go_meeting_test(self):
        self.leader.notice_meeting()

if __name__ == '__main__':
    app = FuncTest()
    app.run()
