from appobject.base import BasePage
from appium.webdriver.common.mobileby import By
from framework.logger import Logger
import time

logger=Logger(logger="OrderCalender").getlog()

#继承BasePage类
class OrderCalender(BasePage):

        #按时间顺序排序
        menu = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon2")  # 点击三条杠进入左侧栏
        menuadd = (By.NAME, "应用设置") #点击应用设置
        calendar_content = (By.ID, "com.pdswp.su.smartcalendar:id/set_timesortnew")  # 点击新日期在前

        # 判断是否排序成功
        equaltexts = (By.ID, "com.pdswp.su.smartcalendar:id/note_time")


        def ordercalendar(self):
            self.click(*self.menu)  # 点击进入左侧栏
            self.click(*self.menuadd)  # 点击应用设置
            time.sleep(3)
            self.click(*self.calendar_content)  # 点击最近日期在前

        def equal_success(self):
            time.sleep(3)
            self.back()  # 返回上一级
            return self.findelement(*self.equaltexts).text
            # print(*self.equaltexts[len(*self.equaltexts)-1]).text)

