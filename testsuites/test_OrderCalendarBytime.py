from testsuites.base_testcase import BaseTestCase
from appobject.orderCalendarBytime import OrderCalender
import unittest
from framework.logger import Logger

logger=Logger(logger="OrderCalenderTest").getlog()

class OrderCalenderTest(BaseTestCase):

    # 测试登录
    def test_order(self):

        orderCal = OrderCalender(self.driver)
        orderCal.ordercalendar()
        try:
            text=orderCal.equal_success()
            if "03月01日" in text:
                logger.info("备忘录排序成功")
        except Exception as e:
            logger.error("排序失败")



if __name__=="__main__":
    unittest.main(verbosity=2)