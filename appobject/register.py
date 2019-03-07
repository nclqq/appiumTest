from appobject.base import BasePage
from appium.webdriver.common.mobileby import By
from framework.logger import Logger
import time

logger=Logger(logger="Register").getlog()

#继承BasePage类
class Register(BasePage):

        #注册
        menu = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon2") #点击三条杠进入左侧栏
        reg_btn=(By.ID,"com.pdswp.su.smartcalendar:id/email") #点击注册
        reg_one_btn = (By.ID, "com.pdswp.su.smartcalendar:id/register")  # 点击注册一个
        username=(By.ID,"com.pdswp.su.smartcalendar:id/username") #输入昵称
        mail_name=(By.ID,"com.pdswp.su.smartcalendar:id/email") #输入邮箱
        pwd = (By.ID, "com.pdswp.su.smartcalendar:id/password") #输入密码
        submit_btn=(By.ID,"com.pdswp.su.smartcalendar:id/reguser") #注册按钮

        #判断是否登录上
        equaltext=(By.ID,"com.pdswp.su.smartcalendar:id/index_ab_title")

        #判断注册失败
        eq_failone=(By.ID,"android:id/body") #弹框
        eq_failtwo = (By.ID, "android:id/progress") #进程

        #登出
        logout_btn=(By.ID,"com.pdswp.su.smartcalendar:id/exit")


    # 输入搜索内容，并提交
        def register(self,username,mailname,pwd):
            self.click(*self.menu)  # 点击进入左侧栏
            self.click(*self.reg_btn)  # 点击进入注册
            self.click(*self.reg_one_btn)  # 点击注册一个
            self.sendkeys(username, *self.username)  # 输入昵称
            self.sendkeys(mailname,*self.mail_name) #输入邮箱
            self.sendkeys(pwd, *self.pwd) #输入密码
            self.click(*self.submit_btn) #点击注册按钮

        def equal_success(self): #判断注册成功
            return self.findelement(*self.equaltext).text

        def eq_regist_fail(self): #判断注册失败，界面存在注册中的旋转框。。。。
            self.findelement(*self.eq_failone)
            self.findelement(*self.eq_failtwo)
            return self.findelement(*self.eq_failtwo)


        #注册成功退出
        def success_logout(self):
            self.click(*self.menu)  # 点击进入左侧栏
            self.click(*self.reg_btn)  # 点击进入用户界面
            time.sleep(3)
            self.click(*self.logout_btn) #点击退出当前账号

        # 注册成功退出
        def fail_logout(self):
            self.back() #如果注册成功，则直接进入智能备忘录界面，则不用返回，若注册失败，则需要
            self.back()
            self.back()


