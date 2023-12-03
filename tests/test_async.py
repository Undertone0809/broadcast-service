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
import unittest

from broadcast_service import broadcast_service


def handle():
    time.sleep(1)


class TestAsync(unittest.TestCase):
    def test_async(self):
        start_time = time.time()
        broadcast_service.enable_async = True
        broadcast_service.listen("test_topic", handle)
        broadcast_service.broadcast("test_topic")
        used_time = time.time() - start_time
        self.assertAlmostEqual(1, used_time, delta=0.1)

    def test_sync(self):
        start_time = time.time()
        broadcast_service.enable_async = False
        broadcast_service.listen("test_topic", handle)
        broadcast_service.broadcast("test_topic")
        used_time = time.time() - start_time
        self.assertEqual(int(used_time), 1)


if __name__ == "__main__":
    unittest.main()
