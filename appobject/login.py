from appobject.base import BasePage
from appium.webdriver.common.mobileby import By
from framework.logger import Logger
import time

logger=Logger(logger="Login").getlog()

#继承BasePage类
class Login(BasePage):

        #登录
        menu = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon2") #点击三条杠进入左侧栏
        reg_btn=(By.ID,"com.pdswp.su.smartcalendar:id/email") #点击进入注册或登陆界面
        pwd = (By.ID, "com.pdswp.su.smartcalendar:id/password")  # 输入密码
        login_btn = (By.ID, "com.pdswp.su.smartcalendar:id/login")  # 登录按钮

        mail_name = (By.ID, "com.pdswp.su.smartcalendar:id/email")  # 邮箱名称

        #判断是否登录上
        equaltext=(By.ID,"com.pdswp.su.smartcalendar:id/index_ab_title")


        def clickmenu(self):
            self.click(*self.menu)  # 点击进入左侧栏
            time.sleep(2)
            self.click(*self.reg_btn)  # 点击进入注册或登录界面

    # 输入搜索内容，并提交
        def login(self,pwd):
            time.sleep(3)
            self.sendkeys(pwd, *self.pwd) #输入密码
            self.click(*self.login_btn) #点击登录按钮
            logger.info("登录成功")

        def login_all(self,mailname,pwd):
            self.clear(*self.mail_name) #清除邮箱
            self.sendkeys(mailname, *self.mail_name)  # 输入邮箱
            self.sendkeys(pwd, *self.pwd) #输入密码
            self.click(*self.login_btn) #点击登录按钮
            logger.info("登录成功")

        def equal_mailname(self): #判断账号是否正确
            time.sleep(2)
            return self.findelement(*self.mail_name).text

        def equal_success(self): #判断是否登陆成功
            time.sleep(3)
            return self.findelement(*self.equaltext).text

