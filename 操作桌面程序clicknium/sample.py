import subprocess
import time
from time import sleep
from clicknium import clicknium as cc, locator, ui

def main():
    '''以下是创建项目时自动生成的代码'''
    # if cc.edge.extension.install_or_update():
    #   print("Please open edge browser to enable clicknium extension, then run sample again.")
    #   return
    #
    # # sample code to demo web automation and desktop application
    # tab = cc.edge.open("https://www.bing.com/")
    # tab.find_element(
    #     locator.sample.bing.search_sb_form_q).set_text('clicknium')
    # tab.find_element(locator.sample.bing.svg).click()
    # sleep(3)
    # tab.close()
    #
    # process = subprocess.Popen("notepad")
    # ui(locator.sample.notepad.document_15).set_text("clicknium")
    '''以上是创建项目时自动生成的代码'''

    tab = cc.chrome.open("https://www.baidu.com/")
    time.sleep(1)
    tab.find_element(locator.sample.baidu.text_kw).set_text('how are you')
    time.sleep(2)
    ui(locator.sample.baidu.submit_su).click()

if __name__ == "__main__":
    main()
