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

import logging
from typing import Optional, List, Callable
from concurrent.futures import ThreadPoolExecutor

__all__ = ['broadcast_service', 'BroadcastService', 'enable_log']


def enable_log():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


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
        self.logger = logging.getLogger(__name__)

        # function renaming
        self.subscribe = self.listen
        self.on = self.listen
        self.publish = self.broadcast
        self.emit = self.broadcast
        self.unsubscribe = self.stop_listen
        self.off = self.stop_listen
        self.on_subscribe = self.on_listen
        self.subscribe_all = self.listen_all
        self.publish_all = self.broadcast_all

    def listen(self, topics: str or List[str], callback: Callable):
        """
        listen topics.
        """
        if type(topics) == str:
            self._invoke_listen_topic(topics, callback)
        elif type(topics) == list:
            for topic in topics:
                self._invoke_listen_topic(topic, callback)
        else:
            raise ValueError("Unknown broadcast-service error, please submit "
                             "issue to https://github.com/Undertone0809/broadcast-service/issues")

    def listen_all(self, callback: Callable):
        """
        '__all__' is a special topic. It can receive any topic message.
        """
        self._invoke_listen_topic('__all__', callback)

    def broadcast(self, topics: str or List[str], *args, **kwargs):
        """
        Launch broadcast on the specify topic
        """
        self.logger.debug(f"[broadcast-service] broadcast topic <{topics}>")
        if type(topics) == str:
            self._invoke_broadcast_topic(topics, *args, **kwargs)
        elif type(topics) == list:
            for topic in topics:
                self._invoke_broadcast_topic(topic, *args, **kwargs)
        else:
            raise ValueError("Unknown broadcast-service error, please submit "
                             "issue to https://github.com/Undertone0809/broadcast-service/issues")

    def broadcast_all(self, *args, **kwargs):
        """
        All topics listened on will be called back.
        Attention: Not all callback function will called. If your publish
         and your subscribe takes different arguments, your callback function
         will not be executed.
        """
        for topic in self.pubsub_channels.keys():
            self._invoke_broadcast_topic(topic, *args, **kwargs)

    def _invoke_listen_topic(self, topic_name: str, callback: Callable):
        if topic_name not in self.pubsub_channels.keys():
            self.pubsub_channels[topic_name] = []

        if callback not in self.pubsub_channels[topic_name]:
            self.pubsub_channels[topic_name].append(callback)

    def _invoke_broadcast_topic(self, topic_name: str, *args, **kwargs):
        """
        broadcast single topic.
        TODO fix problem: There is no guarantee that every callback function will be executed unnecessarily in some cases.
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

    def on_listen(self, topics: str or Optional[List[str]] = None) -> Callable:
        """
        Decorator to listen specify topic. If topics is none, then listen all topics has exits.
        :param topics: topic list, you can input topic like: ["topic1", "topic2"].

        Usage::
            @broadcast_service.on_listen('topic1')
            def handle_all_msg():
                # your code

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
            self.logger.debug(f"[broadcast-service] <{fn.__name__}> listen <{topics}> topic")
            if not topics:
                self.listen_all(fn)
            elif type(topics) == str or list:
                self.listen(topics, fn)

            def inner(*args, **kwargs) -> Callable:
                ret = fn(*args, **kwargs)
                return ret

            return inner

        return decorator


broadcast_service = BroadcastService()
