from getorder import Taobao
import time
from openpyxl import load_workbook
import config

filepath = f'./data/order_data.xlsx'
taobao = Taobao(filepath=filepath)
driver = taobao.broswer()
#老店
# taobao.logintaobao(driver, config.TAOBAO_USERNAME_OLD, config.TAOBAO_PASSWORD_OLD)
#新店
taobao.logintaobao(driver, config.TAOBAO_USERNAME_NEW, config.TAOBAO_PASSWORD_NEW)
try:
    driver.quit()
except:
    pass