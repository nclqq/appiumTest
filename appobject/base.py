from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from framework.logger import Logger
import os
import time



#创建一个logger实例
logger=Logger(logger="BasePage").getlog()

class BasePage(object):

    def __init__(self,driver):
        self.driver=driver

    #后退
    def back(self):
        self.driver.back()
        logger.info("点击后退按钮")

    def quit_browser(self):
        self.driver.quit() #表示断开qppiun的服务器

    # 回车
    def key_return(self):
        self.driver.press_keycode(66)

    #获取屏幕大小
    def getSize(self):
        x=self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x,y)

    # 向上滑动
    def swipeUp(self):
        l = self.getSize()
        x1 = int(l[0] * 0.5) #x坐标
        y1 = int(l[1] * 0.75) #启始y坐标
        y2 = int(l[1] * 0.25) #终点y坐标
        t = 1000
        self.driver.swipe(x1, y1, x1, y2, t)

    # 向下滑动
    def swipeDown(self):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * 0.75)
        t = 1000
        self.driver.swipe(x1, y1, x1, y2, t)

    # 向左滑动
    def swipeRight(self):
        l = self.getSize()
        x1 = int(l[0] * 0.05)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        t = 1000
        self.driver.swipe(x1, y1, x2, y1, t)

    #向左滑动
    def swipeLeft(self):
        l=self.getSize()
        x1=int(l[0]*0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.05)
        t=1000
        self.driver.swipe(x1,y1,x2,y1,t)

    def long_press(self,duration,*loc):
        el=self.findelement(*loc)
        return TouchAction(self.driver).long_press(el).wait(duration).perform()  # 长按

    # 滑动1
    def swipe(self,x1,y1,x2,y2,duration):
        self.driver.swipe(x1, y1, x2, y1, duration)

    # 滑动2
    def click_move(self,x1, y1, x2, y2, time, *loc):
        el=self.findelement(*loc)
        action=TouchAction(self.driver)
        return action.press(el,x1,y1).wait(time).move_to(el,x2,y2).release().perform()


    #获取当前窗口
    def current_window(self):
        current_window=self.driver.current_window_handle
        self.driver.switch_to.window(current_window)

    #滑动屏幕（x1,y1）表示开始的坐标，(x2,y2)表示结束的坐标，t表示持续时间
    def swipe_screen(self,x1,y1,x2,y2,t):
       return self.driver.swipe(x1,y1,x2,y2,t)

    #点击关闭当前窗口
    def close(self):
        try:
            self.driver.close_app()
            logger.info("关闭当前apk")
        except Exception as e:
            logger.error("关闭失败因为 %s"%e)

    #查找元素
    #一个*表示会把一个参数形成一个元组，两个**则会把接收到的参数存入一个字典
    #下面的loc表示元组中的一个值
    def findelement(self,*loc):
        try:
            #next_page=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR , ".page_no:last-of-type")))
            # element = element.find_element(By.ID, ‘foo’)
            # WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info("找到元素 %s"%loc)
        except:
            logger.error("%s 不能找到 %s 元素"%(self,loc))

    #保存图片
    def get_windows_img(self):
        file_path=os.path.dirname(os.path.abspath('.'))+'/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("获取截图并保存到 /screenshots")
        except Exception as e:
            self.get_windows_img()
            logger.error("获取截图失败因为 %s"%e)

    #输入
    def sendkeys(self,text,*loc):
        el=self.findelement(*loc) #调用本类中的方法
        # el.clear()
        try:
            el.send_keys(text)
            logger.info("文本框中写入：%s"%text)
        except Exception as e:
            logger.error("文本框写入失败因为 %s"%e)
            self.get_windows_img()

    #清除文本框
    def clear(self,*loc):
        el=self.findelement(*loc) #调用本类中的方法
        try:
            el.clear()
            logger.info("在写入之前清空文本框")
        except Exception as e:
            logger.error("清空文本框失败因为 %s" % e)
            self.get_windows_img()

    #点击元素
    def click(self,*loc):
        el=self.findelement(*loc) #调用本类中的方法
        try:
            el.click()
        except Exception as e:
            print(e)


