# Copyright (c) 2023 Zeeland
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Copyright Owner: Zeeland
# GitHub Link: https://github.com/Undertone0809/
# Project Link: https://github.com/Undertone0809/broadcast-service
# Contact Email: zeeland@foxmail.com

from broadcast_service import broadcast_service


@broadcast_service.on_listen("topic")
def handle_subscriber_callback():
    print("handle_subscriber_callback")


def handle_publisher_callback(*args):
    print("handle_publisher_callback")


def main():
    broadcast_service.config(
        num_of_executions=5,
        callback=handle_publisher_callback,
        enable_final_return=True,
        interval=0.1,
    ).publish("topic")


if __name__ == "__main__":
    main()
