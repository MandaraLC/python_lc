import time
import uiautomator2 as u2

class Mengchong():
    def __init__(self):
        #usb连接手机
        self.d = u2.connect_usb("83ffe39b")
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
        # x1 = int(self.size[0] * 0.5)
        # y1 = int(self.size[1] * 0.9)
        # y2 = int(self.size[1] * 0.15)
        # self.d.swipe(x1, y1, x1, y2)

    def closeapp(self):
        '''
        关闭钉钉app
        :return:
        '''
        try:
            self.d.app_stop(package_name="com.ys.qzmcxxx2")
        except Exception as e:
            print("报错：", e)
        time.sleep(1)


    def openmengchong(self):
        '''
        打开钉钉app
        :return:
        '''
        #先关闭app，若是打开的了的话
        self.closeapp()

        #启动app
        self.d.app_start(package_name="com.ys.qzmcxxx2")

    #执行程序
    def doit(self):
        for a in range(10000):
            for i in range(10):
                self.d.click(0.075, 0.759)
                self.d.click(0.075, 0.655)
                self.d.click(0.075, 0.603)
                time.sleep(0.3)
            time.sleep(2)
            # 点击少量领取
            self.d.click(0.867, 0.286)
            time.sleep(2)

            self.openmengchong()
            time.sleep(10)
            # if self.d(resourceId="com.ss.android.ugc.aweme:id/yy", text="我").exists(timeout=20):
            #     self.openmengchong()
            #     time.sleep(10)

if __name__ == "__main__":
    mengchong = Mengchong()
    #打开屏幕
    mengchong.screen()
    #打开app
    mengchong.openmengchong()
    #执行程序
    mengchong.doit()