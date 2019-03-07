from testsuites.base_testcase import BaseTestCase
from appobject.deleteCalendar import DeleteCalender
import unittest
from framework.logger import Logger

logger=Logger(logger="DeleteCalenderTest").getlog()

class DeleteCalenderTest(BaseTestCase):

    # 测试登录
    def test_deletaCalen(self):
        deleteCal = DeleteCalender(self.driver)
        deleteCal.deletecalendar()
        try:
            text=deleteCal.equal_success()
            self.assertEqual(text,"智能备忘录",msg=text)
            logger.info("删除备忘录成功")
        except Exception as e:
            logger.error("删除失败")
        deleteCal.recycled_file()
        try:
            text1=deleteCal.equal_success()
            self.assertEqual(text1,"回收站",msg=text1)
            logger.info("清空回收站成功")
        except Exception as e:
            logger.error("清空失败")
        deleteCal.login_out()
        try:
            text = deleteCal.equal_success()
            self.assertEqual(text, "智能备忘录", msg=text)
            logger.info("退出当前账号成功")
        except Exception as e:
            logger.error("退出当前账号失败或账号未登录")




if __name__=="__main__":
    unittest.main(verbosity=2)