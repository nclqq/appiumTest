from testsuites.base_testcase import BaseTestCase
from appobject.searchCalendar import SearchCalender
import unittest
from framework.logger import Logger
from selenium.webdriver.common.keys import Keys

logger=Logger(logger="SearchCalendarTest").getlog()

class SearchCalendarTest(BaseTestCase):

    # 测试登录
    def test_search(self):
        #声明HomePage类对象
        searchCal = SearchCalender(self.driver)
        searchCal.searchcalendar("dd")
        try:
            text=searchCal.equal_success()
            self.assertIn("dd",text)   # assertIn(a,b) a in b
            logger.info("搜索备忘录成功")
        except Exception as e:
            logger.error("搜索失败或搜索的内容不存在")



if __name__=="__main__":
    unittest.main(verbosity=2)