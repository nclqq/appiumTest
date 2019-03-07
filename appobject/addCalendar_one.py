from appobject.base import BasePage
from appium.webdriver.common.mobileby import By
from framework.logger import Logger
import time

logger=Logger(logger="AddCalenderOne").getlog()

#继承BasePage类
class AddCalenderOne(BasePage):

        #第一种方法添加备忘录
        menu = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon2") #点击三条杠进入左侧栏
        reg_btn=(By.ID,"com.pdswp.su.smartcalendar:id/design_menu_item_text") #点击添加备忘
        calendar_content = (By.ID, "com.pdswp.su.smartcalendar:id/add_input_content")  # 输入备忘内容
        sure_click = (By.ID, "com.pdswp.su.smartcalendar:id/quick_add")  # 点击对勾

        # 判断是否添加成功
        equaltext = (By.ID, "com.pdswp.su.smartcalendar:id/index_ab_title")


        def addcalendar(self,calendarContent):
            self.click(*self.menu)  # 点击进入左侧栏
            time.sleep(2)
            self.click(*self.reg_btn)  # 点击进入注册或登录界面
            time.sleep(3)
            self.sendkeys(calendarContent, *self.calendar_content)  # 输入备忘内容
            time.sleep(3)
            self.click(*self.sure_click)  # 点击对勾

        def equal_success(self):
            time.sleep(3)
            return self.findelement(*self.equaltext).text

