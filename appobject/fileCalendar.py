from appobject.base import BasePage
from appium.webdriver.common.mobileby import By
from framework.logger import Logger
from appium.webdriver.common.touch_action import TouchAction
import time

logger=Logger(logger="FileCalender").getlog()

#继承BasePage类
class FileCalender(BasePage):

    one_li = (By.ID, "com.pdswp.su.smartcalendar:id/note_title")  #选中某一个
    fileCan = (By.ID, "com.pdswp.su.smartcalendar:id/menu_archive")  # 点击归档

    # 判断是否归档成功
    eq_file = (By.NAME, "归档成功")

    #查找归档
    menu = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon2")  # 点击三条杠进入左侧栏
    menufile = (By.NAME, "归档") #点击归档



    return_btn=(By.ID, "com.pdswp.su.smartcalendar:id/menu") #点击恢复
    # 判断是否添加成功
    equal_return = (By.NAME, "备忘录取消回档")


    def filecalendar(self):
        self.long_press(2000,*self.one_li) #长按
        self.click(*self.fileCan)  # 点击归档

    def return_file(self):
        self.click(*self.menu)  # 点击进入左侧栏
        self.click(*self.menufile)  # 点击归档
        self.click(*self.one_li) #查看归档中的备忘录详细信息
        self.back() #返回上一级
        time.sleep(3)
        self.swipe(602,162,297,164,1000) #左滑方法一
        # self.click_move(602,162,297,164,1000,*self.one_li) #左滑方法二
        self.click(*self.return_btn) #点击恢复

    #判断归档成功
    def equal_filesuccess(self):
        return self.findelement(*self.eq_file).text

    #判断回档成功
    def equal_retuensuccess(self):
        return self.findelement(*self.equal_return).text


