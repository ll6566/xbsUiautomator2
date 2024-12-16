import os
from time import sleep


def wait_dev(dev, timeout_=60):
    # 等待设备在线
    for t in range(timeout_):
        sleep(2)
        if dev in os.popen("adb devices").read():
            return True
