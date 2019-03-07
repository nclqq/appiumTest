from appobject.base import BasePage
from appium.webdriver.common.mobileby import By
from framework.logger import Logger
import time

logger=Logger(logger="AddCalenderTwo").getlog()

#继承BasePage类
class AddCalenderTwo(BasePage):

        #第二种方法添加备忘录
        menuadd = (By.ID, "com.pdswp.su.smartcalendar:id/menuAdd") #点击右下角的加号
        calendar_content = (By.ID, "com.pdswp.su.smartcalendar:id/add_input_content")  # 输入备忘内容
        sure_click = (By.ID, "com.pdswp.su.smartcalendar:id/quick_add")  # 点击对勾

        # 判断是否添加成功
        equaltext = (By.ID, "com.pdswp.su.smartcalendar:id/index_ab_title")


        def addcalendar(self,calendarContent):
            self.click(*self.menuadd)  # 点击右下角的加号
            time.sleep(3)
            self.sendkeys(calendarContent, *self.calendar_content)  # 输入备忘内容
            time.sleep(3)
            self.click(*self.sure_click)  # 点击对勾

        def equal_success(self):
            time.sleep(3)
            return self.findelement(*self.equaltext).text

