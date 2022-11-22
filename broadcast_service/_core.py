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

from concurrent.futures import ThreadPoolExecutor

__all__ = ['broadcast_service']

class BroadcastService:
    """
    This class implements broadcast mode, you can import the instance by single class.
    By BroadcastService, you can send topic message,it will automatically execute the
    callback function if some classes subscribe the topic.

    example:
    app.py
    ---------------------------------------------------------------------------------
    from broadcast_service import broadcast_service

    def handle_msg(params):
        print(params)

    if __name__ == '__main__':
        info = 'This is very important msg'

        # listen topic
        broadcast_service.listen('Test', handle_msg)

        # publish broadcast
        broadcast_service.broadcast('Test', info)
    ---------------------------------------------------------------------------------

    """

    def __init__(self):
        """
        subscribe_info example:

        subscribe_info = {
            'my_topic': [{
                'callback_function': function1,
                'params': {
                    'name':'jack',
                    'age':20
                }
            },{
                'callback_function': function2,
                'params': 666
            }]
        }
        """
        self.topic_list = []
        self.subscribe_info = {}
        self.enable_async = True
        self.thread_pool = ThreadPoolExecutor(max_workers=5)

    def listen(self, topic_name, callback):
        """ listen topic """
        if topic_name not in self.subscribe_info.keys():
            self.subscribe_info[topic_name] = []

        if callback not in self.subscribe_info[topic_name]:
            options = {
                'callback_function': callback,
            }
            self.subscribe_info[topic_name].append(options)

    def broadcast(self, topic_name, *args, **kwargs):
        """ Launch broadcast on the specifide topic """
        if topic_name not in self.topic_list:
            self.topic_list.append(topic_name)

        if topic_name not in self.subscribe_info.keys():
            return

        for item in self.subscribe_info[topic_name]:
            if self.enable_async:
                self.thread_pool.submit(item['callback_function'], *args, **kwargs)
            else:
                item['callback_function'](*args, **kwargs)

    def stop_listen(self, topic_name, callback):
        if topic_name not in self.subscribe_info.keys():
            raise RuntimeError("you didn't listen the topic:", topic_name)
        if callback not in self.subscribe_info[topic_name]:
            pass
        else:
            self.subscribe_info[topic_name].remove(callback)

broadcast_service = BroadcastService()
