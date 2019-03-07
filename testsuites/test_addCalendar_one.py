from testsuites.base_testcase import BaseTestCase
from appobject.addCalendar_one import AddCalenderOne
import unittest
from framework.logger import Logger

logger=Logger(logger="AddCalendarOneTest").getlog()

class AddCalendarOneTest(BaseTestCase):

    # 测试登录
    def test_addCalenOne(self):
        addCal = AddCalenderOne(self.driver)
        addCal.addcalendar("the first calendar")
        try:
            text=addCal.equal_success()
            self.assertEqual(text,"智能备忘录",msg=text)
            logger.info("添加备忘录成功")
        except Exception as e:
            logger.error("添加失败")



if __name__=="__main__":
    unittest.main(verbosity=2)