#coding=UTF-8
import requests
import urllib3
import time
import re
from lxml import etree
#不打印warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) 
#登录时需要POST的数据
data = {'username':'', 
        'password':'', 
        'loginfield':'username',
        'refer':'https://bbs.uestc.edu.cn/'}
#设置请求头
headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
#登录时表单提交到的地址
login_url='https://bbs.uestc.edu.cn/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LcBaK&inajax=1'
url = 'https://bbs.uestc.edu.cn/forum.php?mod=forumdisplay&fid=174'

def login():
        session = requests.Session()
        resp = session.post(login_url, data,verify =False)
        print(resp.content.decode('utf-8'))       
        pattern=r"欢迎您回来"
        m = re.search(pattern, resp.content.decode('utf-8'))
        if m.start()>0:
                print("login_success at "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        return session
session=login()
while(1):
        resp = session.get(url)
        html = etree.HTML(resp.content)     
        success_login = html.xpath('//div[@id="messagetext"]/p/text()')  
        if success_login and success_login[0][0:2]=="抱歉": 
                print("Connection disconnected at "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                print("Reconnecting...")
                session = login()
                time.sleep(300) #防止出现验证码 
        else:print("login continue at "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        time.sleep(45)  




  



