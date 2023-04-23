## OnHook

河畔挂机脚本，断线自动重连
--------------------------------------------------
4/8更新
之前版本出现了session过期后访问报错的情况
已更新新版本  经验证能正确重连
![image](https://user-images.githubusercontent.com/52741194/233853456-d2ec112e-581b-408c-80c4-f410c5f93fe5.png)
## 环境

- python3

- lxml
- requests
- urllib3

## 运行
### linux服务器端
1.在onhook.py  data中填写账号密码
填用户名 使用邮箱或者uid登录需要自行更改loginfield 
```
data = {'username':'', 
        'password':'', 
        'loginfield':'username',
        'refer':'https://bbs.uestc.edu.cn/'}
```

2.上传至云服务器

```
nohup python3 -u onHook.py
```

退出ssh终端，程序后台运行即可 输出信息默认保存到nohup.out文件中
运行成功后重新进入终端在同目录下nohup.out下查看是否成功登录以及运行状态
```
cat nohup.out
```
![image](https://user-images.githubusercontent.com/52741194/233853565-e5ac676a-0be6-4b5f-8de0-fd0fbf278410.png)
### windows端
输入账号密码后直接运行即可
