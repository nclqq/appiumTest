from testsuites.base_testcase import BaseTestCase
from appobject.register import Register
import unittest
from framework.logger import Logger

logger=Logger(logger="UserRegisterTest").getlog()

class UserRegisterTest(BaseTestCase):

    # 测试登录
    def test_register(self):

        register = Register(self.driver)
        #注册失败
        register.register("4","4@csdn.com","44444444")
        try:
            text1 = register.eq_regist_fail()
            self.assertTrue(text1)
            logger.info("该邮箱已被注册")
        except Exception as e:
            logger.error("断言异常：%s"%e)
        register.fail_logout()
        text = register.equal_success()
        self.assertEqual(text, "智能备忘录", msg=text)
        logger.info("返回成功")



        # 注册成功
        # register.register("5", "5@csdn.com", "55555555")
        # try:
        #     text=register.equal_success()
        #     self.assertEqual(text,"智能备忘录",msg=text)
        #     logger.info("用户注册成功")
        # except Exception as e:
        #     logger.error("断言异常：%s" % e)
        # register.success_logout()  # 退出当前账号
        # try:
        #     text = register.equal_success()
        #     self.assertEqual(text, "智能备忘录", msg=text)
        #     logger.info("退出当前账号成功")
        # except Exception as e:
        #     logger.error("退出当前账号失败或账号未登录")






if __name__=="__main__":
    unittest.main(verbosity=2)