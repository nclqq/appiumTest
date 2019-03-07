import sys
sys.path.append("E:\appiumTest")

import unittest
import os
import HTMLTestRunner

from testsuites.test_register import UserRegisterTest
from testsuites.test_login import testuserLogin
from testsuites.test_changeUserName import ChangeUserNameTest
from testsuites.test_addCalendar_one import AddCalendarOneTest
from testsuites.test_SearchCalendar import SearchCalendarTest
from testsuites.test_OrderCalendarBytime import OrderCalenderTest
from testsuites.test_fileCalendar import FileCalendarTest
from testsuites.test_DeleteCalendar import DeleteCalenderTest


#设置报告文件保存路径
current_path=os.path.dirname(os.path.realpath(__file__)) #获取当前路径（用例路径）
report_path=os.path.join(current_path,"report") #设置报告路径，并且路径名是report(报告存放路径)
if not os.path.exists(report_path):
    os.mkdir(report_path)


# 构造测试套件
suite=unittest.TestSuite() #创建套件
suite.addTest(unittest.makeSuite(UserRegisterTest)) #增加注册测试
suite.addTest(unittest.makeSuite(testuserLogin)) #增加登录测试
suite.addTest(unittest.makeSuite(ChangeUserNameTest)) #增加修改用户名测试
suite.addTest(unittest.makeSuite(AddCalendarOneTest)) #增加备忘录测试
suite.addTest(unittest.makeSuite(SearchCalendarTest)) #增加搜索备忘录测试
suite.addTest(unittest.makeSuite(OrderCalenderTest)) #增加备忘录排序测试
suite.addTest(unittest.makeSuite(FileCalendarTest)) #增加归档备忘录测试
suite.addTest(unittest.makeSuite(DeleteCalenderTest)) #增加删除备忘录测试

#测试用例目录
# file_path = os.path.dirname(os.path.abspath("."))  # 获取要安装的apk包
# suite_path = file_path + '/testsuites' # 要测试的apk包的路径
#加载测试用例
# suite=unittest.TestLoader().discover(suite_path,pattern='test_*.py')




if __name__=="__main__":
    #打开一个文件，将result写入此file中
    html_report=report_path+r"\result.html" #（html报告文件路径）
    fp=open(html_report,"wb")
    #初始化一个htmltestrunner实例对象，用来生成报告
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="用例执行情况")
    runner.run(suite)