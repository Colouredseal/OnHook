## OnHook

河畔挂机脚本，每45秒刷新一次，断线自动重连

## 环境

- python3

- lxml
- requests
- urllib3

## 运行

1.在onhook.py  data中填写账号密码

```
data = {'username':'', 
        'password':'', 
        'loginfield':'username',
        'refer':'https://bbs.uestc.edu.cn/'}
```

2.上传至云服务器

```
nohup python3 -u onhook.py
```

后台运行即可
