from testsuites.base_testcase import BaseTestCase
from appobject.fileCalendar import FileCalender
import unittest
from framework.logger import Logger

logger=Logger(logger="FileCalendarTest").getlog()

class FileCalendarTest(BaseTestCase):

    def test_fileCalen(self):
        fileCal = FileCalender(self.driver)
        fileCal.filecalendar() #归档
        try:
            text=fileCal.equal_filesuccess()
            self.assertEqual(text,"归档成功",msg=text)
            logger.info("归档成功")
        except Exception as e:
            logger.error("归档失败")
        fileCal.return_file()  # 恢复
        try:
            text1 = fileCal.equal_retuensuccess()
            self.assertEqual(text1, "备忘录取消回档", msg=text1)
            logger.info("恢复成功")
        except Exception as e:
            logger.error("恢复失败")



if __name__=="__main__":
    unittest.main(verbosity=2)