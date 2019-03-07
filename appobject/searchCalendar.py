from appobject.base import BasePage
from appium.webdriver.common.mobileby import By
from framework.logger import Logger
import time
from selenium.webdriver.common.keys import Keys

logger=Logger(logger="SearchCalender").getlog()

#继承BasePage类
class SearchCalender(BasePage):

        #第一种方法添加备忘录
        search_btn = (By.ID, "com.pdswp.su.smartcalendar:id/toolbar_search") #点击搜索按钮
        search_input=(By.ID,"android:id/search_src_text") #搜索框


        calendar_content = (By.ID, "com.pdswp.su.smartcalendar:id/add_input_content")  # 输入备忘内容
        sure_click = (By.ID, "com.pdswp.su.smartcalendar:id/quick_add")  # 点击对勾

        # 判断是否搜索成功
        equaltext = (By.ID, "com.pdswp.su.smartcalendar:id/note_title")


        def searchcalendar(self,searchContent):
            self.click(*self.search_btn)  # 点击搜索按钮
            time.sleep(2)
            self.sendkeys(searchContent, *self.search_input)  # 输入搜索内容并回车
            time.sleep(1)
            self.key_return() #回车

        def equal_success(self):
            time.sleep(3)
            return self.findelement(*self.equaltext).text
