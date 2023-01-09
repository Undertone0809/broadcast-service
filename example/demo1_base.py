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

from broadcast_service import broadcast_service, BroadcastService


def handle_no_msg():
    print("handle_no_msg func")


def callback_of_no_params():
    """
    callback of no parameters
    """
    # listen topic
    broadcast_service.subscribe('no_params', handle_no_msg)

    # publish broadcast
    broadcast_service.publish('no_params')
    """
    other way:
    bc = BroadcastService()
    bc.listen('no_params', handle_no_msg)
    bc.broadcast('no_params')
    """


@broadcast_service.on_listen(["decorator", "lambda"])
def handle_decorator(*args, **kwargs):
    print("handle_no_msg func")


def callback_of_decorator():
    """
    callback of decorator
    """
    broadcast_service.broadcast("decorator")


def callback_of_lambda():
    """
    callback of lambda
    """
    # listen topic
    broadcast_service.listen('lambda', lambda x,y: print(f"the params is {x} and {y}"))

    # publish broadcast
    broadcast_service.broadcast('lambda', 11, 22)


def handle_2msg(info, info2):
    print("handle_2msg func")
    print(info)
    print(info2)


def callback_of_2params():
    """
    callback of 2 parameters
    """
    info = 'info'
    info2 = 'info2'

    # listen topic
    broadcast_service.listen('2_params', handle_2msg)

    # publish broadcast
    broadcast_service.broadcast('2_params', info, info2)


def main():
    callback_of_no_params()
    # callback_of_decorator()
    # callback_of_lambda()
    # callback_of_2params()


if __name__ == '__main__':
    main()
