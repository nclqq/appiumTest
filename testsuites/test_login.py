from testsuites.base_testcase import BaseTestCase
from appobject.login import Login
import unittest
from framework.logger import Logger
from framework.util import Utils
from ddt import ddt,data,unpack


logger=Logger(logger="testuserLogin").getlog()
logindata=Utils.read_excel("E:/appiumTest/data/logindata.xlsx","Sheet1")

@ddt
class testuserLogin(BaseTestCase):

    # 测试登录
    @data(*logindata)
    def test_login(self,data):
        login = Login(self.driver)
        login.clickmenu() #点击进入登录界面
        loginName=data["mailname"]
        print(loginName)
        loginPwd=data["pwd"]
        print(loginPwd)
        if login.equal_mailname() is loginName:
            login.login(loginPwd)  #如果邮箱账号正确，只输入密码
        else:
            login.login_all(loginName,loginPwd) #如果邮箱账号不正确，清空账号，输入账号和密码
        try:
            text=login.equal_success()
            self.assertEqual(text,"智能备忘录",msg=text)
            logger.info("用户登录成功")
        except Exception as e:
            logger.error("注册失败或用户已存在")




if __name__=="__main__":
    unittest.main(verbosity=2)