import os
from time import sleep


def wait_dev(dev, timeout_=60):
    for t in range(timeout_):
        if dev in os.popen("adb devices").read():
            return True
        sleep(1)
