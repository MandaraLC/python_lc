'''
uiautomator2 怎么wifi连接手机，参考：
https://www.jianshu.com/p/ea633818247c
'''
import time
import uiautomator2 as u2


class Mengchong():
    def __init__(self):
        #usb连接手机
        # self.d = u2.connect_usb("83ffe39b")
        self.d = u2.connect_adb_wifi("192.168.1.103:5566")
        # self.d = u2.connect("http://192.168.1.68")
        #打印设备信息
        print("设备信息：", self.d.device_info)
        #屏幕大小
        self.size = self.d.window_size()
        # self.handle_watcher()

    def handle_watcher(self):
        """定义一个监控器"""
        # 监控器会单独的起一个线程
        # 用户隐私协议
        self.d.watcher.when('').click()
        # 监控器写好之后，要通过start方法来启动
        self.d.watcher.start()

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
            self.d.app_stop(package_name="com.sh.shuihulu.kiwi")
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
        self.d.app_start(package_name="com.sh.shuihulu.kiwi")

    # #执行程序
    def doit(self):
        #点击聊天
        #//*[@resource-id="com.sh.shuihulu.kiwi:id/ll_bottom"]
        time.sleep(3)
        self.d.click(0.692, 0.949)
        # 在获取到y轴远方点，获取到y轴近点
        for a in range(5000):
            for i in range(7):
                try:
                    print(f"{a}---=====----{i}")
                    # 点亮屏幕
                    self.d.screen_on()
                    self.d.xpath(f'//*[@resource-id="com.sh.shuihulu.kiwi:id/recyclerview"]/android.widget.LinearLayout[{i+1}]/android.view.ViewGroup[1]').click_exists(timeout=2)
                    time.sleep(1)
                    self.d.xpath('//*[@resource-id="com.sh.shuihulu.kiwi:id/all_et_content_container"]').click_exists(timeout=2)
                    time.sleep(1)
                    self.d.xpath('//*[@resource-id="com.sh.shuihulu.kiwi:id/all_et_content_container"]').set_text("你在干嘛呢，下班了吗")
                    #点击发送
                    self.d.click(0.781, 0.824)
                    time.sleep(1)
                    self.d.xpath('//*[@resource-id="com.sh.shuihulu.kiwi:id/iv_top_left"]').click_exists(timeout=2)
                    time.sleep(1)
                except Exception as e:
                    try:
                        self.d.xpath('//*[@resource-id="com.sh.shuihulu.kiwi:id/iv_top_left"]').click_exists(timeout=2)
                    except:
                        pass
                    try:
                        self.d.xpath('//android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]').click_exists(timeout=2)
                    except:
                        pass
                    print("报错", e)
            x1 = int(self.size[0] * 0.5)
            y1 = int(self.size[1] * 0.9)
            y2 = int(self.size[1] * 0.15)
            self.d.swipe(x1, y1, x1, y2)  # 从下往上滑动
            time.sleep(2)

if __name__ == "__main__":
    mengchong = Mengchong()
    #打开屏幕
    mengchong.screen()
    #打开app
    # mengchong.openmengchong()
    # 执行程序
    mengchong.doit()