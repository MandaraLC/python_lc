import time
import uiautomator2 as u2

#钉钉打卡类
class Dingdingdaka():
    def __init__(self):
        #usb连接手机
        self.d = u2.connect_usb("abfa90600406")
        # self.d = u2.connect("http://192.168.1.68")
        #打印设备信息
        print("设备信息：", self.d.device_info)
        #屏幕大小
        self.size = self.d.window_size()

    def screen(self):
        '''
        点亮屏幕和解锁
        :return:
        '''
        # 点亮屏幕
        self.d.screen_on()
        #从下往上滑
        x1 = int(self.size[0] * 0.5)
        y1 = int(self.size[1] * 0.9)
        y2 = int(self.size[1] * 0.15)
        self.d.swipe(x1, y1, x1, y2)

    def closeapp(self):
        '''
        关闭钉钉app
        :return:
        '''
        try:
            self.d.app_stop(package_name="com.alibaba.android.rimet")
        except Exception as e:
            print("报错：", e)
        time.sleep(1)
    def opendingding(self):
        '''
        打开钉钉app
        :return:
        '''
        #先关闭app，若是打开的了的话
        self.closeapp()

        #启动app
        self.d.app_start(package_name="com.alibaba.android.rimet")
        time.sleep(2)
        self.d.app_clear("com.alibaba.android.rimet")
        print("已清除app缓存")
        self.d.app_stop("com.tal.kaoyan")

if __name__ == "__main__":
    ding = Dingdingdaka()
    ding.screen()
    time.sleep(2)
    ding.opendingding()


