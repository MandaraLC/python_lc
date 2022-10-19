import time
from pywinauto.keyboard import send_keys
from pywinauto import application

#打开exe程序
# app = application.Application(backend='uia').start(r'C:\Program Files (x86)\AliWorkbench\AliWorkbench.exe')
# wx_win = app.window(class_name='StandardFrame')
# wx_win.print_control_identifiers(depth=None, filename=None)
# wx_win.child_window(title="登 录", control_type="Button").click_input()

#根据进程pid
app = application.Application(backend='uia').connect(process=23744)
print(app)
wx_win = app.window(class_name='StandardFrame')
wx_win.print_control_identifiers(depth=None, filename=None)

#搜索框
searchinput = wx_win.child_window(auto_id="1324", control_type="Edit")
#发送消息框
send_msg = wx_win.child_window(auto_id="1372", control_type="Edit")
#输入内容搜索
keywords = 'x梦幻花朵'

for i in range(10):
    searchinput.click_input()
    send_keys("^a")
    searchinput.type_keys(keywords)
    time.sleep(0.5)
    send_keys("{VK_RETURN}")

    time.sleep(1)

    send_msg.click_input()
    send_keys("^a")
    send_msg.type_keys(f"第{i+1}次-----你好，这是测试发送文本")
    time.sleep(1)