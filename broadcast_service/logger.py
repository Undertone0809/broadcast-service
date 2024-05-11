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

import datetime
import os
import sys
import tempfile

from loguru import logger as _logger

from broadcast_service.singleton import Singleton


def convert_backslashes(path: str):
    """Convert all \\ to / of file path."""
    return path.replace("\\", "/")


def get_default_storage_path(module_name: str = "") -> str:
    pne_storage_path = os.path.expanduser("~/.broadcast_service")

    if not os.path.exists(pne_storage_path):
        try:
            os.makedirs(pne_storage_path)
        except PermissionError:
            pne_storage_path = f"{tempfile.gettempdir()}/broadcast_service"

    return convert_backslashes(f"{pne_storage_path}/{module_name}")


def get_log_path() -> str:
    log_directory = get_default_storage_path("logs")
    current_time = datetime.datetime.now().strftime("%Y%m%d")
    return f"{log_directory}/{current_time}.log"


def enable_log():
    logger.remove()

    logger.add(get_log_path(), level="DEBUG")
    logger.add(sys.stderr, level="DEBUG")


class Logger(metaclass=Singleton):
    def __init__(self) -> None:
        self.logger = _logger

        self.logger.remove()

        self.logger.add(get_log_path(), level="DEBUG")
        self.logger.add(sys.stderr, level="WARNING")


logger = Logger().logger
