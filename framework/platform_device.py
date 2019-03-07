import os
import time
from configparser import ConfigParser
from appium import webdriver
from framework.logger import Logger

logger=Logger(logger="PlatformDevice").getlog()

class PlatformDevice:

    def __init__(self):

        self.desired_caps = {}  # 创建字典
        apk_path = os.path.dirname(os.path.abspath("."))  # 获取要安装的apk包
        self.desired_caps['app'] = apk_path + '/app/znbwl.apk' # 要测试的apk包的路径


    # 在配置文件中读取设备类型并返回该设备
    def open_device(self):

        config = ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini' # 绝对路径
        config.read(file_path, encoding='utf-8')# 读取文件

        # 选择设备
        self.desired_caps['platformName']=config.get("platformType", "platformName") # 是Android设备还是ios设备
        logger.info("你选择了 %s 设备" % config.get("platformType", "platformName"))
        self.desired_caps['platformVersion'] = config.get("platformType", "platformVersion")  # 设备版本
        logger.info("设备版本： %s" % config.get("platformType", "platformVersion"))
        self.desired_caps['deviceName'] = config.get("platformType", "deviceName")  # 设备名称
        logger.info("设备名称： %s" % config.get("platformType", "deviceName"))

        self.desired_caps['sessionOverride'] = config.get("equalOvrride", "sessionOverride") # 表示每次生成的session进行覆盖
        self.desired_caps['noReset'] = config.get("equalOvrride", "noReset") # 为true表示不需要每次都安装apk文件

        self.desired_caps['appPackage'] =config.get("apkName", "appPackage") # todolist.apk的name(利用aapt命令查看)
        self.desired_caps['appActivity'] =config.get("apkName", "appActivity") # todolist.apk的launchName(启动name)(利用aapt命令查看)

        #设置可输入中文
        self.desired_caps['unicodeKeyboard'] = config.get("inputType", "unicodeKeyboard")
        self.desired_caps['resetKeyboard'] = config.get("inputType", "resetKeyboard")

        url = config.get("testURL", "URL")

        self.driver = webdriver.Remote(url, self.desired_caps)  # 利用webdriver的remote方法启动app, 并传递json键值对
        logger.info('启动设备并打开apk')

        # self.driver.maximize_window()
        # logger.info("最大化当前窗口")
        # self.driver.implicitly_wait(10)
        # logger.info("设置隐式等待10秒")

        return self.driver


    def quit_device(self):
        self.driver.quit()
        logger.info("关闭并退出")


# PlatformDevice().open_device()
# PlatformDevice().quit_device()