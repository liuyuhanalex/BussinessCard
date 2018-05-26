import requests
import ssl,sys
import base64
import importlib
import os,re
import time

importlib.reload(sys)

#1.GET THE access_token FROM BAIDU-API
def get_access_token():
    host =  'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=dGqa7vM8RgIVE89yr0cPXBWs&client_secret=VQkK9attUyP5QppIvvLMGg8rC8S67ISe'
    headers = {
        'Content-Type':'application/json;charset=UTF-8'
    }
    res = requests.get(url=host,headers=headers).json()
    return res['access_token']

#Root folder to store images of bussiness card
root = r"C:\Users\liuyu\Desktop\BussinessCard\Cards"

#Result folder to store text result
resultFolder = r"C:\Users\liuyu\Desktop\BussinessCard\Result"

count = 0

url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'

data = {}
access_token = get_access_token()
data['access_token']=access_token

#Deal with all the images in the folder
for i in os.listdir(root):
    file = open(os.path.join(root,i),"rb")
    image = file.read()
    file.close()

    data['image'] = base64.b64encode(image)
    headers={
        "Content-Type":"application/x-www-form-urlencoded",
        "apikey":"dGqa7vM8RgIVE89yr0cPXBWs"
    }
    try:
        res = requests.post(url=url,headers=headers,data=data)
    except:
        time.sleep(5)
        res = requests.post(url=url,headers=headers,data=data)

    result = res.json()
    filename = i[:-4]
    with open(os.path.join(resultFolder,"{}.txt".format(filename)),"a",encoding='utf8') as f:
        for line in result["words_result"]:
            f.write(line["words"]+"\n")
    count+=1
    print("Already finish {}!".format(count))
