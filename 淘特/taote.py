import time
import uiautomator2 as u2

#钉钉打卡类
class Taotedaka():
    def __init__(self):
        #usb连接手机
        self.d = u2.connect_usb("83ffe39b")
        # self.d = u2.connect("http://192.168.1.68")
        #打印设备信息
        print("设备信息：", self.d.device_info)
        #屏幕大小
        self.size = self.d.window_size()

    def closeapp(self):
        '''
        关闭钉钉app
        :return:
        '''
        try:
            self.d.app_stop(package_name="com.taobao.litetao")
        except Exception as e:
            print("报错：", e)
        time.sleep(1)

    def screen(self):
        '''
        点亮屏幕和解锁
        :return:
        '''
        # 点亮屏幕
        self.d.screen_on()
        # 从下往上滑
        # x1 = int(self.size[0] * 0.5)
        # y1 = int(self.size[1] * 0.9)
        # y2 = int(self.size[1] * 0.15)
        # self.d.swipe(x1, y1, x1, y2)

    def opentaote(self):
        '''
        打开钉钉app
        :return:
        '''
        #先关闭app，若是打开的了的话
        self.closeapp()
        time.sleep(5)
        #启动app
        self.d.app_start(package_name="com.taobao.litetao")
        time.sleep(6)
        self.d(resourceId="com.taobao.litetao:id/fl_default").click_exists(timeout=10)
        time.sleep(10)
        for i in range(100):
            print(f"点击赚钱{i+1}")
            self.d(text="点击赚钱").click_exists(timeout=10)
            time.sleep(10)

if __name__ == "__main__":
    ding = Taotedaka()
    # 打开屏幕
    ding.screen()
    time.sleep(2)
    #打卡淘特
    ding.opentaote()