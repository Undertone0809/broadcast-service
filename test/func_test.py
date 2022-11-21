# Copyright 2022 Zeeland(https://github.com/Undertone0809/). All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
