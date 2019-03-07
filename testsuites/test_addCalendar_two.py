from testsuites.base_testcase import BaseTestCase
from appobject.addCalendar_two import AddCalenderTwo
import unittest
from framework.logger import Logger

logger=Logger(logger="addCalendarTwoTest").getlog()

class addCalendarTwoTest(BaseTestCase):

    # 测试登录
    def test_addCalenTwo(self):
        #声明HomePage类对象
        addCal = AddCalenderTwo(self.driver)
        addCal.addcalendar("the second calendar")
        try:
            text=addCal.equal_success()
            self.assertEqual(text,"智能备忘录",msg=text)
            logger.info("添加备忘录成功")
        except Exception as e:
            logger.error("添加失败")



if __name__=="__main__":
    unittest.main(verbosity=2)