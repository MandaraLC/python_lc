'''
一、uiautomator2 怎么wifi连接手机，参考：
https://www.jianshu.com/p/ea633818247c
1.usb连接到电脑，执行adb tcpip 5566 (执行结果：restarting in TCP mode port: 5566 )
2.断开USB，执行adb connect 192.168.1.103:5566 （192.168.1.103是手机的局域网IP地址）
3.u2.connect_adb_wifi("192.168.1.103:5566")

二、获取正在运行的app的包名：
adb shell dumpsys window | findstr mCurrentFocus
'''
import time
import uiautomator2 as u2

class Huanyou():
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
                    #self.d.click(0.515, 0.554)
                    self.d(text="我知道了").click_exists(timeout=1)
                    time.sleep(0.2)
                    self.d.xpath('//*[@resource-id="com.sh.shuihulu.kiwi:id/all_et_content_container"]').click_exists(timeout=2)
                    time.sleep(1)
                    self.d.xpath('//*[@resource-id="com.sh.shuihulu.kiwi:id/all_et_content_container"]').set_text("吃午饭了吗~")
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
                    print("报错", e)
                    break
            x1 = int(self.size[0] * 0.5)
            y1 = int(self.size[1] * 0.9)
            y2 = int(self.size[1] * 0.15)
            self.d.swipe(x1, y1, x1, y2)  # 从下往上滑动
            time.sleep(2)

if __name__ == "__main__":
    huanyou = Huanyou()
    #打开屏幕
    huanyou.screen()
    #打开app
    # huanyou.openmengchong()
    # 执行程序
    huanyou.doit()