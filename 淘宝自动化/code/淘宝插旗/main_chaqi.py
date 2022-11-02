from chaqi import Flaginsertion
import time

# 实例化
filepath = f'./excel/淘宝插旗{time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))}.xlsx'
taobao = Flaginsertion(filepath=filepath)
#读取数据
allorder = taobao.getorderdata(excelpath='./data/淘宝插旗.xlsx')
if len(allorder[0]) > 0 or len(allorder[1]) > 0:
    # 初始化excel
    taobao.initexcel()

#这是老店的订单数据
if len(allorder[0]) > 0:
    # 实例化
    driver = taobao.broswer()
    shoptype = 1 #1-老店 2-新店
    # 登录淘宝
    taobao.logintaobao(driver, allorder[0], shoptype)
    try:
        driver.quit()
    except:
        pass
else:
    print("老店没有数据")

#这是新店的订单数据
if len(allorder[1]) > 0:
    # 实例化
    driver = taobao.broswer()
    shoptype = 2 #1-老店 2-新店
    # 登录淘宝
    taobao.logintaobao(driver, allorder[1], shoptype)
    try:
        driver.quit()
    except:
        pass
else:
    print("新店没有数据")