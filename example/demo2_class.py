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
"""
This example show how to use in a class. The ueage is very
similar to the common method.
"""


from broadcast_service import broadcast_service


class Person:

    def __init__(self, name: str) -> None:
        self.name = name

    def subscribe(self, topic):
        broadcast_service.listen(topic, self.take_milk)
        print(f"{self.name} subscribe the milk service")

    def take_milk(self):
        print(f"{self.name} takes the milk")


class Market:

    def send_milk(self):
        print("Market send milk")
        broadcast_service.broadcast("milk")


def main():
    p1 = Person("Jack")
    p1.subscribe("milk")
    p2 = Person("Tom")
    p2.subscribe("milk")
    m = Market()
    m.send_milk()


if __name__ == '__main__':
    main()
