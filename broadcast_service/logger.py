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
import logging
import os
import platform
import tempfile

__all__ = ["get_logger", "enable_log_no_file", "enable_log"]
logger = logging.getLogger("cushy-storage")


def get_logger():
    return logger


def get_project_root_path() -> str:
    """get project root path"""
    project_path = os.getcwd()
    max_depth = 10
    count = 0
    while not os.path.exists(os.path.join(project_path, "README.md")):
        project_path = os.path.split(project_path)[0]
        count += 1
        if count > max_depth:
            return os.getcwd()
    return project_path


STORAGE_PATH = {"PROJECT_ROOT": get_project_root_path(), "CURRENT": "./"}


def get_default_storage_path(
    file_name: str, root_path: str = STORAGE_PATH["PROJECT_ROOT"]
) -> str:
    if platform.system() == "Windows":
        return f"{root_path}/{file_name}"
    elif platform.system() == "Linux" or "Darwin":
        dir_path = os.environ.get("TMPDIR")
        if not dir_path:
            dir_path = tempfile.gettempdir()
        dir_path = os.path.join(dir_path, "broadcast_service")
        return f"{dir_path}/{file_name}"
    else:
        return f"./{file_name}"


def get_default_log_path() -> str:
    return get_default_storage_path("log")


def _check_log_path():
    """check whether log file exist"""
    if not os.path.exists(get_default_log_path()):
        os.makedirs(get_default_log_path())


def get_log_name() -> str:
    _check_log_path()
    cur_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{get_default_log_path()}/log_{cur_time}.log"


def enable_log():
    """enable logging to terminal and file"""
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s - %(asctime)s:%(message)s -",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(f"{get_log_name()}", mode="w", encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )


def enable_log_no_file():
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(levelname)s] %(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
