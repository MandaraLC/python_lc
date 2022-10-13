import uiautomator2 as u2
import time
from apscheduler.schedulers.blocking import BlockingScheduler

d = u2.connect_adb_wifi("127.0.0.1:62001")


def click_text(self, str, sq=0):  # 对于无法直接点击的控件写了个函数
    path = d(text=str)[sq]
    x, y = path.center()
    d.click(x, y)


def click(card_ty=''):
    d.app_start("com.alibaba.android.rimet")  # 启动应用
    time.sleep(5)
    d(text="工作台").click()
    time.sleep(3)
    d(text="考勤打卡").click()
    # time.sleep(3)
    # d(scrollable=True).fling.toEnd()
    # click_text(d, card_ty, -1)
    # time.sleep(3)
    # d.screenshot("11.jpg")
    # d.push("11.jpg", "/sdcard/0/11.jpg")
    # d.app_stop("com.alibaba.android.rimet")
    # send_info()

click()

# def send_info():  # 将打卡信息截图利用小号发送给自己大号
#     d.app_start("com.tencent.mm")  # 启动应用
#     time.sleep(5)
#     click_text(d, "通讯录")
#     click_text(d, "打卡")
#     click_text(d, "发消息")
#     time.sleep(2)
#     d(description="更多功能按钮，已折叠").click()
#     time.sleep(2)
#     d.swipe(1000, 1450, 100, 1450)
#     time.sleep(2)
#     click_text(d, "文件")
#     time.sleep(2)
#     click_text(d, "微信文件", -1)
#     click_text(d, "手机存储")
#     click_text(d, "0")
#     d(resourceId="com.tencent.mm:id/cvh").click()
#     d(text="发送(1/9)").click()
#     d(text="给朋友留言").click()
#     d.send_keys("今日打卡记录，请注意查收", clear=True)
#     d(text="发送").click()
#     time.sleep(5)
#     d.app_stop("com.tencent.mm")
#
#
# def job1():
#     click("上班打卡")
#
#
# def job2():
#     click("下班打卡")
#
#
# if __name__ == "__main__":
#     sched = BlockingScheduler()  # 设置定时任务，周一至周五 上午8.50自动打上班卡，下午6.10自动打下班卡
#     sched.add_job(job1, 'cron', day_of_week='mon-fri', hour='9', minute='00')
#     sched.add_job(job2, 'cron', day_of_week='mon-fri', hour='18', minute='30')
#     sched.start()