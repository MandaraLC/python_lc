#验证码破解
import requests
import json
import base64
import time

clientKey = "5d343f5a4ddbfa12ec1824685c1d4f037adb6ea11865" #帐户密钥，可以在个人中心找到

type = "ImageToTextTask" #验证码类型

class CoscoCaptcha:
    #获取图片base64值
    def imgbase64(self, imgurl):
        image_base64 = ''
        with open(imgurl, 'rb') as f:
            image = f.read()
            image_base64 = str(base64.b64encode(image), encoding='utf-8')
        return image_base64

    #post请求
    def postRequest(self, url, data):
        respone = requests.post(url = url, json = data)
        return respone

    #创建识别任务
    def createTask(self, image_base64):
        url = "https://api.yescaptcha.com/createTask"
        data = {
            "clientKey":clientKey,
            "task": #下面写你需要识别的类型
                {
                    "type":type,
                    "body":image_base64
                }
        }
        respone = self.postRequest(url, data)
        return respone

    #获取识别结果
    def getTaskResult(self, taskId):
        url = "https://api.yescaptcha.com/getTaskResult"
        data = {
            "clientKey": clientKey,
            "taskId": taskId
        }
        respone = self.postRequest(url, data)
        return respone

    #破解验证码
    def pojie(self, imgurl):
        image_base64 = self.imgbase64(imgurl)
        # 创建任务, 并获取taskId
        createTask_respone = self.createTask(image_base64)
        createTask_json = json.loads(createTask_respone.text)

        # 根据taskId得到识别结果
        getTaskResult_respone = self.getTaskResult(createTask_json['taskId'])
        getTaskResult_json = json.loads(getTaskResult_respone.text)
        if "solution" in getTaskResult_json:
            return getTaskResult_json['solution']['text']
            #print(getTaskResult_json['solution']['text'])
        else:
            return False

if __name__ == '__main__':
    while True:
        # 获取图片的base64值
        imgurl = './image.png'
        coscoCaptcha = CoscoCaptcha()
        pojie = coscoCaptcha.pojie(imgurl)

        if pojie:
            print(pojie)
        else:
            print("解析失败！")

        time.sleep(3)

