from appium import webdriver
from framework.platform_device import PlatformDevice
import unittest
import warnings


class BaseTestCase(unittest.TestCase):


    # setUp()主要是测试的前提准备工作
    def setUp(self):
        self.be=PlatformDevice()
        warnings.simplefilter('ignore',ResourceWarning)
        self.driver=self.be.open_device()


    #测试结束后的操作
    def tearDown(self):
        self.be.quit_device()
