# -*- coding: utf-8 -*-
# @Time    : 2023/6/14 12:15
# @Author  : Zeeland
# @File    : test_publisher_callback.py
# @Software: PyCharm
import time
from unittest import TestCase

from broadcast_service import broadcast_service


class TestPublisherCallback(TestCase):
    def test_num_of_execution_no_params_no_subscriber(self):
        self.publisher_counter = 0
        self.subscriber_counter = 0

        @broadcast_service.on_listen("no_params_no_subscriber")
        def handle_subscriber_callback():
            self.subscriber_counter += 1

        def handle_publisher_callback():
            self.publisher_counter += 1

        broadcast_service.config(
            num_of_executions=5, callback=handle_publisher_callback
        ).publish("no_params_no_subscriber")

        self.assertEqual(5, self.publisher_counter)
        self.assertEqual(5, self.subscriber_counter)

    def test_num_of_execution_takes_return_params_and_subscriber(self):
        self.publisher_counter = 0
        self.subscriber_counter = 0

        @broadcast_service.on_listen("takes_return_params_and_subscriber")
        def handle_subscriber_callback():
            self.subscriber_counter += 1
            return {"sub_counter": self.subscriber_counter}

        def handle_publisher_callback(*args):
            self.publisher_counter += 1
            self.assertEqual(len(args), self.publisher_counter)

        broadcast_service.config(
            num_of_executions=5, callback=handle_publisher_callback
        ).publish("takes_return_params_and_subscriber")

        self.assertEqual(5, self.subscriber_counter)
        self.assertEqual(5, self.publisher_counter)

    def test_enable_final_return(self):
        self.counter = 0

        def handle_publisher_callback():
            self.counter += 1

        broadcast_service.config(
            num_of_executions=5,
            callback=handle_publisher_callback,
            enable_final_return=True,
        ).publish("what ever....")
        self.assertEqual(1, self.counter)

    def test_interval(self):
        start_time = time.time()
        self.counter = 0

        @broadcast_service.on_listen("test_interval")
        def handle_subscriber_callback():
            self.counter += 1

        broadcast_service.config(num_of_executions=5, interval=0.2).publish(
            "test_interval"
        )

        duration = time.time() - start_time
        self.assertAlmostEqual(1, duration, delta=0.1)
        self.assertEqual(5, self.counter)

    def test_split_parameter(self):
        self.counter = 1

        @broadcast_service.on_listen("test_split_parameter")
        def handle_subscriber_callback(**kwargs):
            self.assertEqual(self.counter, kwargs["split_parameter"])
            self.counter += 1

        params = [1, 2, 3]
        broadcast_service.config(num_of_executions=3, split_parameters=params).publish(
            "test_split_parameter"
        )
