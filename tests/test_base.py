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

import time
from unittest import TestCase
from broadcast_service import broadcast_service
from broadcast_service.logger import get_logger, enable_log

logger = get_logger()


def wait(seconds=0.1):
    time.sleep(seconds)


class TestBroadcast(TestCase):
    def test_listen_of_common(self):
        self.test_listen_of_common_no_params = False
        self.test_listen_of_common_specify_params = False
        self.test_listen_multi_topic1_of_common = False
        self.test_listen_multi_topic2_of_common = False
        self.counter = 0
        self.all_counter = 0

        def handle_topic_no_params():
            self.test_listen_of_common_no_params = True

        def handle_topic_specify_params(a, b, c):
            self.assertEqual(11, a)
            self.assertEqual(22, b)
            self.assertEqual(33, c)
            self.test_listen_of_common_specify_params = True

        def handle_multi_topics(*args, **kwargs):
            self.counter += 1
            if args[0] == 111:
                self.test_listen_multi_topic1_of_common = True
            if args[0] == 222:
                self.test_listen_multi_topic2_of_common = True

        def handle_all_topics(*args, **kwargs):
            self.all_counter += 1

        # test all topics
        broadcast_service.subscribe_all(handle_all_topics)

        # test listen of common no params
        broadcast_service.subscribe(
            "test_listen_of_common_no_params", handle_topic_no_params)
        broadcast_service.publish("test_listen_of_common_no_params")
        wait()
        self.assertTrue(self.test_listen_of_common_no_params)

        # test listen of common specify params
        broadcast_service.subscribe(
            "test_listen_of_common_specify_params", handle_topic_specify_params)
        broadcast_service.publish(
            "test_listen_of_common_specify_params", 11, 22, 33)
        wait()
        self.assertTrue(self.test_listen_of_common_specify_params)

        # test listen multi topics of common
        topics = ['test_listen_multi_topic1_of_common', 'test_listen_multi_topic2_of_common']
        broadcast_service.subscribe(topics, handle_multi_topics)
        broadcast_service.publish("test_listen_multi_topic1_of_common", 111)
        broadcast_service.publish("test_listen_multi_topic2_of_common", 222)
        wait()
        self.assertTrue(self.test_listen_multi_topic1_of_common)
        self.assertTrue(self.test_listen_multi_topic2_of_common)
        self.assertEqual(2, self.counter)

        self.assertEqual(4, self.all_counter)

    def test_listen_of_decorator(self):
        self.test_listen_of_decorator_no_params1 = False
        self.test_listen_of_decorator_no_params2 = False
        self.test_listen_of_decorator_multi_params = False
        self.test_listen_of_decorator_specify_params = False
        self.test_listen_of_decorator_listen_all = False
        self.counter = 0

        @broadcast_service.on_listen("test_listen_of_decorator_no_params1")
        def handle_topic_no_params():
            self.test_listen_of_decorator_no_params1 = True

        @broadcast_service.on_listen(["test_listen_of_decorator_no_params2"])
        def handle_topic_no_params():
            self.test_listen_of_decorator_no_params2 = True

        @broadcast_service.on_listen(["test_listen_of_decorator_no_params1", "test_listen_of_decorator_no_params2"])
        def handle_topic_no_params():
            if self.test_listen_of_decorator_no_params1 and self.test_listen_of_decorator_no_params2:
                self.test_listen_of_decorator_multi_params = True

        @broadcast_service.on_listen(["test_listen_of_decorator_specify_params"])
        def handle_topic_specify_params(a, b, c):
            self.assertEqual(11, a)
            self.assertEqual(22, b)
            self.assertEqual(33, c)
            self.test_listen_of_decorator_specify_params = True

        @broadcast_service.on_listen()
        def handle_listen_all_topics(*args, **kwargs):
            self.counter += 1
            self.test_listen_of_decorator_listen_all = True

        broadcast_service.publish("test_listen_of_decorator_no_params1")
        wait()
        self.assertTrue(self.test_listen_of_decorator_no_params1)

        broadcast_service.publish("test_listen_of_decorator_no_params2")
        wait()
        self.assertTrue(self.test_listen_of_decorator_no_params2)

        wait()
        self.assertTrue(self.test_listen_of_decorator_multi_params)

        broadcast_service.publish(
            "test_listen_of_decorator_specify_params", 11, 22, 33)
        wait()
        self.assertTrue(self.test_listen_of_decorator_specify_params)

        broadcast_service.publish("test_listen_of_decorator_listen_all")
        wait()
        self.assertTrue(self.test_listen_of_decorator_listen_all)
        self.assertEqual(4, self.counter)

    def test_listen_of_lambda(self):
        self.test_listen_of_lambda_no_params = False
        self.test_listen_of_lambda_specify_params = False

        def handle_topic_no_params():
            self.test_listen_of_lambda_no_params = True

        def handle_topic_specify_params(params: bool):
            self.test_listen_of_lambda_specify_params = params

        broadcast_service.subscribe(
            "test_listen_of_lambda_no_params", lambda: handle_topic_no_params())
        broadcast_service.publish("test_listen_of_lambda_no_params")
        wait()
        self.assertTrue(self.test_listen_of_lambda_no_params)

        broadcast_service.subscribe(
            "test_listen_of_lambda_specify_params", lambda: handle_topic_specify_params(True))
        broadcast_service.publish("test_listen_of_lambda_specify_params")
        wait()
        self.assertTrue(self.test_listen_of_lambda_no_params)

    def test_broadcast(self):
        self.test_broadcast_one_topic1 = False
        self.test_broadcast_one_topic2 = False
        self.test_broadcast_multi_topic1 = False
        self.test_broadcast_multi_topic2 = False
        self.counter = 0

        @broadcast_service.on_listen("test_broadcast_one_topic1")
        def handle_one_topic1():
            self.counter += 1
            self.test_broadcast_one_topic1 = True

        @broadcast_service.on_listen("test_broadcast_one_topic2")
        def handle_one_topic2():
            self.counter += 1
            self.test_broadcast_one_topic2 = True

        @broadcast_service.on_listen("test_broadcast_multi_topic1")
        def handle_multi_topic1():
            self.counter += 1
            self.test_broadcast_multi_topic1 = True

        @broadcast_service.on_listen("test_broadcast_multi_topic2")
        def handle_multi_topic2():
            self.counter += 1
            self.test_broadcast_multi_topic2 = True

        broadcast_service.publish("test_broadcast_one_topic1")
        wait()
        self.assertTrue(self.test_broadcast_one_topic1)

        broadcast_service.publish(["test_broadcast_one_topic2"])
        wait()
        self.assertTrue(self.test_broadcast_one_topic2)

        broadcast_service.publish(["test_broadcast_multi_topic1", "test_broadcast_multi_topic2"])
        wait()
        self.assertTrue(self.test_broadcast_multi_topic1 and self.test_broadcast_multi_topic2)

        broadcast_service.publish_all()
        wait()
        self.assertEqual(8, self.counter)

    def test_broadcast_multiple_call_one_topic(self):
        self.counter = 0

        @broadcast_service.on_listen("test_broadcast_multiple_call_one_topic")
        def handle_multi_topic1():
            self.counter += 1
            self.test_broadcast_multi_topic1 = True

        broadcast_service.config(num_of_executions=5).publish("test_broadcast_multiple_call_one_topic")
        wait()
        self.assertTrue(5, self.counter)
