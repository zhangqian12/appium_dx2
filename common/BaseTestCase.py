#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from appium import webdriver
from conf import appium_config

class AppTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': appium_config.CONNECT['platformName'],
            'platformVersion': appium_config.CONNECT['platformVersion'],
            'deviceName': appium_config.CONNECT['deviceName'],
            'appPackage': appium_config.CONNECT['appPackage'],
            'appActivity': appium_config.CONNECT['appActivity']
        }
        self.driver = webdriver.Remote(appium_config.CONNECT['baseUrl'], desired_caps)

    def tearDown(self):
        self.driver.quit()
