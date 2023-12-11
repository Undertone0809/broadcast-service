import unittest
from concurrent.futures import ThreadPoolExecutor

from broadcast_service import BroadcastService


class TestInvokeCallback(unittest.TestCase):
    def setUp(self):
        self.broadcast_service = BroadcastService()
        self.thread_pool = ThreadPoolExecutor(max_workers=5)
        self.callback1 = lambda x: x * 2
        self.callback2 = lambda x: x + 2

    def test_invoke_callback_async(self):
        result = self.broadcast_service._invoke_callback(self.callback1, self.thread_pool, True, 5)
        self.assertEqual(result, 10)

    def test_invoke_callback_sync(self):
        result = self.broadcast_service._invoke_callback(self.callback1, self.thread_pool, False, 5)
        self.assertEqual(result, 10)

    def test_multiple_callbacks(self):
        self.broadcast_service.listen('Test', self.callback1)
        self.broadcast_service.listen('Test', self.callback2)
        self.broadcast_service.broadcast('Test', 5)
        self.assertEqual(self.broadcast_service.pubsub_channels['Test'][0](5), 10)
        self.assertEqual(self.broadcast_service.pubsub_channels['Test'][1](5), 7)

    def tearDown(self):
        self.thread_pool.shutdown()

if __name__ == '__main__':
    unittest.main()
