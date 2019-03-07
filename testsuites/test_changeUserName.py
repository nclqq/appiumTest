from testsuites.base_testcase import BaseTestCase
from appobject.changeUserName import ChangeUserName
import unittest
from framework.logger import Logger

logger=Logger(logger="ChangeUserNameTest").getlog()

class ChangeUserNameTest(BaseTestCase):

    # 测试登录
    def test_change(self):
        change = ChangeUserName(self.driver)
        change.changeUserName("235")
        try:
            text=change.equal_changed_success()
            self.assertEqual(text,"235",msg=text)
            logger.info("用户名修改成功")
        except Exception as e:
            logger.error("用户名修改失败")




if __name__=="__main__":
    unittest.main(verbosity=2)