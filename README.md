## OnHook

河畔挂机脚本，每45秒刷新一次，断线自动重连
4/2更新
之前版本出现了session过期后访问报错的情况
已更新新版本

## 环境

- python3

- lxml
- requests
- urllib3

## 运行

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

后台运行即可 输出信息默认保存到nohup.out文件中
运行成功后在同目录下nohup.out下查看是否成功登录以及运行状态
![U@H$F@@0@$F3XZKQ_C7 BRH](https://user-images.githubusercontent.com/52741194/225537953-56aa204a-3bbf-4c21-9dfc-9eb5906a59da.png)
