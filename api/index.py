# -*- codeing = utf-8 -*-
# @Time : 2021/01/21 9:05 上午
# @Author : Zfour
# @File : spyder1.py
# @Software : PyCharm

import leancloud
from http.server import BaseHTTPRequestHandler
import json

def getdata():
    leancloud.init("LwmvjzvHzUxmJDK6QeAlflA4-MdYXbMMI", "CsDY3h7a7GYktVFH3yO8vpsd")
    # 验证密钥
    Aqidata = leancloud.Object.extend('aqidata')
    # 连接class
    query = Aqidata.query
    # 为查询创建别名
    query.descending('createdAt')
    # 选择排序方式
    query.limit(24)
    # 限定数量
    query.select('data','time')
    # 选择类
    query_list = query.find()
    # 执行查询，返回数组
    datalist=[]
    for i in query_list:
        itemlist=[]
        data = i.get('data')
        time = i.get('time')
        itemlist.append(time)
        itemlist.append(data)
        datalist.append(itemlist)
    return datalist

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = getdata()
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return
