from appobject.base import BasePage
from appium.webdriver.common.mobileby import By
from framework.logger import Logger
import time

logger=Logger(logger="ChangeUserName").getlog()

#继承BasePage类
class ChangeUserName(BasePage):

        #修改用户名
        menu = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon2") #点击三条杠进入左侧栏
        reg_btn=(By.ID,"com.pdswp.su.smartcalendar:id/email") #点击进入注册或登陆界面
        user_btn = (By.ID, "com.pdswp.su.smartcalendar:id/title")  # 点击用户

        changetext=(By.ID, "com.pdswp.su.smartcalendar:id/username") #修改用户名
        sure_click=(By.ID, "com.pdswp.su.smartcalendar:id/quick_add") #点击对勾

        equal_changed=(By.ID,"com.pdswp.su.smartcalendar:id/username") #判断是否修改成功


        def changeUserName(self,change_username):
            self.click(*self.menu)  # 点击进入左侧栏
            time.sleep(2)
            self.click(*self.reg_btn)  # 点击进入注册或登录界面
            self.click(*self.user_btn)  # 点击进入修改用户名界面
            self.sendkeys(change_username, *self.changetext)  # 输入修改的用户名
            time.sleep(3)
            self.click(*self.sure_click)  # 点击对勾


        def equal_changed_success(self): #判断用户名是否修改成功
            time.sleep(2)
            return self.findelement(*self.equal_changed).text


