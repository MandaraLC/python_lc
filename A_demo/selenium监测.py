from selenium import webdriver
import random
import time
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "none"

chromeOptions = webdriver.ChromeOptions()
#windows
chromeOptions.add_argument('--remote-debugging-port=' + str(random.randint(10000, 20000)))
# chromeOptions.add_experimental_option("debuggerAddress", "127.0.0.1:9222") #手动打开浏览器
# chromeOptions.add_argument('disable-infobars')
# chromeOptions.add_argument("window-size=1920,1080")
chromeOptions.add_experimental_option('useAutomationExtension', False)
chromeOptions.add_experimental_option('excludeSwitches', ['enable-automation'])
chromeOptions.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36')
driver = webdriver.Chrome(options=chromeOptions)
driver.maximize_window()  # 窗口最大化显示
# 绕过浏览器指纹
stealth(driver, languages=["en-US", "en"], vendor="Google Inc.", platform="Win32", webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine", fix_hairline=True, )
# 输入 stealth.min.js 文件路径
# with open('./stealth.min.js') as f:
#     js = f.read()
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     "source": js
# })
driver.get("https://bot.sannysoft.com/")
# driver.save_screenshot("123.png")

# driver.get("http://www.baidu.com")
# driver.find_element(by=By.XPATH, value="//input[@id='kw']").send_keys("龙猫")
# time.sleep(1)
# driver.find_element(by=By.XPATH, value="//input[@class='bg s_btn']").click()

time.sleep(10)
driver.quit()
