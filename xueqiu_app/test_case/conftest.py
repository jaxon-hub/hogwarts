"""
__author__ = 'jaxon'
__time__ = '2020/6/17 9:04 下午'
"""
import os
import shlex
import signal

import allure
import pytest
import subprocess

@pytest.fixture(scope="class", autouse=True)
def record():
    cmd = shlex.split("scrcpy --no-display --record tmp.mp4")
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    yield
    os.kill(p.pid, signal.SIGTERM)
    with open("tmp.mp4", "rb") as f:
        content = f.read()
    allure.attach(content, attachment_type=allure.attachment_type.MP4)