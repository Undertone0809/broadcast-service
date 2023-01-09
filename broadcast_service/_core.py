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
from functools import wraps
from typing import Optional, List, Callable

__all__ = ['broadcast_service', 'BroadcastService']


class BroadcastService:
    """
    This class implements broadcast mode, you can import the instance by single class.
    By BroadcastService, you can send topic message,it will automatically execute the
    callback function if some classes subscribe the topic.

    example:
    ---------------------------------------------------------------------------------
    from broadcast_service import broadcast_service

    def handle_msg(params):
        print(params)

    if __name__ == '__main__':
        info = 'This is very important msg'

        # listen topic
        broadcast_service.subscribe('Test', handle_msg)

        # publish broadcast
        broadcast_service.publish('Test', info)
    ---------------------------------------------------------------------------------
    """

    def __init__(self):
        """
        pubsub_channels is the dict to store publish/subscribe data.
        pubsub_channels example:

        pubsub_channels = {
            'my_topic': [callback_function1: Callable,callback_function2: Callable]
            '__all__': [callback_function3: Callable]
        }
        """
        self.pubsub_channels: dict = {
            '__all__': []
        }
        self.enable_async: bool = True
        self.thread_pool = ThreadPoolExecutor(max_workers=5)

        # function renaming
        self.subscribe = self.listen
        self.publish = self.broadcast
        self.unsubscribe = self.stop_listen

        self.on = self.listen
        self.emit = self.broadcast
        self.off = self.stop_listen

    def listen(self, topic_name: str, callback: Callable):
        """ listen topic """
        if topic_name not in self.pubsub_channels.keys():
            self.pubsub_channels[topic_name] = []

        if callback not in self.pubsub_channels[topic_name]:
            # options = {
            #     'callback_function': callback,
            # }
            self.pubsub_channels[topic_name].append(callback)

    def broadcast(self, topic_name: str, *args, **kwargs):
        """
        Launch broadcast on the specify topic
        """
        if topic_name not in self.pubsub_channels.keys():
            self.pubsub_channels[topic_name] = []

        for item in self.pubsub_channels[topic_name]:
            if self.enable_async:
                self.thread_pool.submit(
                    item, *args, **kwargs)
            else:
                item(*args, **kwargs)

        for item in self.pubsub_channels['__all__']:
            if self.enable_async:
                self.thread_pool.submit(
                    item, *args, **kwargs)
            else:
                item(*args, **kwargs)

    def stop_listen(self, topic_name: str, callback: Callable):
        if topic_name not in self.pubsub_channels.keys():
            raise RuntimeError("you didn't listen the topic:", topic_name)
        if callback not in self.pubsub_channels[topic_name]:
            pass
        else:
            self.pubsub_channels[topic_name].remove(callback)

    def on_listen(self, topics: Optional[List[str]] = None) -> Callable:
        """
        Decorator to listen specify topic. If topics is none, then listen all topics has exits.
        :param topics: topic list, you can input topic like: ["topic1", "topic2"].

        Usage::
            @broadcast_service.on_listen(['topic1'])
            def handle_all_msg():
                # your code

            @broadcast_service.on_listen(['topic1','topic2'])
            def handle_all_msg():
                # your code

            @broadcast_service.on_listen()
            def handle_all_msg(*args, **kwargs):
                # your code

        Attention: Your params should keep '*args, **kwargs'. If you publish a topic take arguments,
        the callback function you handle should take arguments, otherwise it will not be called back.
        """
        def decorator(fn: Callable) -> Callable:
            if topics is not None:
                for topic in topics:
                    self.listen(topic, fn)
            else:
                self.listen('__all__', fn)

            def inner(*args, **kwargs) -> Callable:
                ret = fn(*args, **kwargs)
                return ret
            return inner
        return decorator


broadcast_service = BroadcastService()
