import time
import uiautomator2 as u2

#钉钉打卡类
class Dingdingdaka():
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
        x1 = int(self.size[0] * 0.5)
        y1 = int(self.size[1] * 0.9)
        y2 = int(self.size[1] * 0.15)
        self.d.swipe(x1, y1, x1, y2)

    def opendingding(self):
        '''
        打开钉钉app
        :return:
        '''
        #先关闭app，若是打开的了的话
        self.closeapp()

        #启动app
        self.d.app_start(package_name="com.alibaba.android.rimet")
        #点击打卡按钮
        self.d.xpath('//*[@resource-id="com.alibaba.android.rimet:id/tab_container"]/android.widget.LinearLayout[4]').click_exists(timeout=10)

        #获取当前时间
        now = time.strftime("%H%M%S", time.localtime(time.time()))
        print(f"当前时分秒：{time.strftime('%H:%M:%S', time.localtime(time.time()))}")

        # 上、下班时分秒
        sbtime = '090000'
        xbtime = '183000'
        print("上班时分秒：09:00:00")
        print("下班时分秒：18:30:00")

        #识别当前是否在09:00-18:30之间（当前时间>上班时间，并且当前时间<下班时间）
        if int(now) > int(sbtime) and int(now) < int(xbtime):
            print("目前处于上班时间", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
        elif int(now) >= int(xbtime):
            print("已下班！可以打卡了")
            #点击下班打卡
            self.d.xpath('//*[@resource-id="__react-content"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.view.View[1]').click_exists(timeout=5)
            time.sleep(1)
        elif int(now) <= int(sbtime):
            print("上班打卡！")
            # 点击下班打卡
            self.d.xpath('//*[@resource-id="__react-content"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.view.View[1]').click_exists(timeout=5)
            time.sleep(1)

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

if __name__ == "__main__":
    ding = Dingdingdaka()
    #打开屏幕
    ding.screen()
    #钉钉打开
    ding.opendingding()
    time.sleep(5)
    #退出app
    ding.closeapp()

