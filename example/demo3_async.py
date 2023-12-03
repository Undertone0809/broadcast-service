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

import random
import time

from broadcast_service import broadcast_service


class Application:
    """
    This demo shows how to use async.
    Scene:
        One day, leader Tom arrive the company but find not one staff in company
        because all staff are playing outside. Therefor, Tom send a message
        everyone must must return to company now. Jack, Jasmine, Jane go back
        now when they receive the message. Actually, they need different time to go back
        in different places and they need to declare that they are back when they back.
    Attention:
        broadcast-service is asynchronous by defalut. If you want to close the async
        state. You can use:
            broadcast_service.enable_async = False
        to close the async statement.

    """

    def __init__(self):
        self.leader = Leader("Tom")
        self.staff1 = Staff("Jack")
        self.staff2 = Staff("Jasmine")
        self.staff3 = Staff("Jane")
        self.current_time = None

    def run(self):
        self.current_time = time.time()
        self.leader.notice_go_back()


def print_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


class Leader:
    def __init__(self, name):
        self.name = name

    def notice_go_back(self):
        print("[{1}] {0}(leader) notice meeting now.".format(self.name, print_time()))
        meeting_info = "You guys must go back now!"
        broadcast_service.broadcast("meeting", meeting_info)


class Staff:
    def __init__(self, name):
        self.name = name
        broadcast_service.listen("meeting", self.go_back)

    def go_back(self, info):
        print(
            "[{2}] {0}(staff) receive msg '{1}' and go back now.".format(
                self.name, info, print_time()
            )
        )
        time.sleep(2)
        print("[{1}] {0}(staff) is back now.".format(self.name, print_time()))


def main():
    broadcast_service.enable_async = False
    app = Application()
    app.run()


if __name__ == "__main__":
    main()
