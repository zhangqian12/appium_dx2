#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import time
import re
from appium import webdriver

sys.path.append("..")
# 用于解决多个手机连接问题
from common.mobile import get_serialno

# Read mobile deviceId
device_id = get_serialno()

# Read mobile os Version
os_version = os.popen('adb -s {0} shell getprop ro.build.version.release'.format(device_id)).read()


def appium_start():
    config = {
        'platformName': 'Android',  # 平台
        'platformVersion': os_version,  # 系统版本
        'deviceName': device_id,  # 测试设备ID
        'appPackage':'com.diaox2.android',
        'appActivity':'com.diaox2.android.activity.SplashActivity',
        # 'app':'D:\com.jiuai.apk',   # apk 路径
        'newCommandTimeout': 30,
        'automationName': 'Appium',
        'unicodeKeyboard': True,  # 编码,可解决中文输入问题
        'resetKeyboard': True,
        'baseurl':"http://localhost:4723/wd/hub"}
    return webdriver.Remote('http://localhost:4723/wd/hub', config)
