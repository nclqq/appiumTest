from appobject.base import BasePage
from appium.webdriver.common.mobileby import By
from framework.logger import Logger
from appium.webdriver.common.touch_action import TouchAction
import time

logger=Logger(logger="DeleteCalender").getlog()

#继承BasePage类
class DeleteCalender(BasePage):

    one_li = (By.ID, "com.pdswp.su.smartcalendar:id/note_title")  #选中某一个
    deleteCan = (By.ID, "com.pdswp.su.smartcalendar:id/menu_delete")  # 点击删除

    # 判断是否删除成功
    equaltext = (By.ID, "com.pdswp.su.smartcalendar:id/index_ab_title")


    #查找归档
    menu = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon2")  # 点击三条杠进入左侧栏
    menufile = (By.NAME, "回收站") #点击回收站


    clear_btn=(By.ID, "com.pdswp.su.smartcalendar:id/button") #点击清空回收站

    alert_area = (By.ID, "com.pdswp.su.smartcalendar:id/material_background")  # 进入alert弹窗中
    btn_area = (By.ID, "com.pdswp.su.smartcalendar:id/buttonLayout")  # 进入alert弹窗中的button区域
    sure_btn=(By.NAME,"确定") #确定按钮

    # 登出
    reg_btn = (By.ID, "com.pdswp.su.smartcalendar:id/email")  # 点击注册登陆界面
    logout_btn = (By.ID, "com.pdswp.su.smartcalendar:id/exit") #退出当前账户按钮

    def deletecalendar(self):
        el=self.findelement(*self.one_li)
        TouchAction(self.driver).long_press(el).wait(2000).perform() #长按
        self.click(*self.deleteCan)  # 点击删除

    def recycled_file(self):
        self.click(*self.menu)  # 点击进入左侧栏
        self.click(*self.menufile)  # 点击回收站
        time.sleep(2)
        self.click(*self.one_li) #查看
        self.back()
        time.sleep(2)
        elem=self.findelement(*self.one_li).text
        if elem is not "":
            self.click(*self.clear_btn) #点击清空回收站
            self.findelement(*self.alert_area) #弹窗区域
            self.findelement(*self.alert_area) #button区域
            self.click(*self.sure_btn) #点击确定按钮



    def equal_success(self):
        time.sleep(3)
        return self.findelement(*self.equaltext).text

    def login_out(self):
        self.back()
        self.click(*self.menu)  # 点击进入左侧栏
        self.click(*self.reg_btn)  # 点击进入用户界面
        time.sleep(3)
        self.click(*self.logout_btn)  # 点击退出当前账号

