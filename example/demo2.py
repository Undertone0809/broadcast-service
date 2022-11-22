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

def handle_msg(info, info2):
    print(info)
    print(info2)

if __name__ == '__main__':
    info = 'This is very important msg'
    info2 = 'This is also a very important msg.'

    # listen topic
    broadcast_service.listen('Test', handle_msg)

    # publish broadcast
    broadcast_service.broadcast('Test', info, info2)
