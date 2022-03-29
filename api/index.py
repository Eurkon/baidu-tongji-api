# -*- coding: utf-8 -*-
# @Author    : Eurkon
# @Date      : 2021/6/5 10:19

import os
import json
import sys
import requests
import leancloud
from urllib import parse
from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler


def get_data(params):
    """重定向请求百度统计，解决跨域问题

    Args:
        params (dict): {site_id: 网站id, access_token: token, ...}

    Returns:
        json: 百度统计返回的网页统计数据
    """

    if 'access_token' not in params:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sys.path.append(BASE_DIR)
        # 通过 LeanCloud 获取百度统计 Access Token
        app_id = os.environ["APPID"]  # LeanCloud AppID
        app_key = os.environ["APPKEY"]  # LeanCloud AppKey
        leancloud.init(app_id, app_key)
        token = leancloud.Object.extend('BaiduToken')
        query = token.query
        query.select('accessToken')
        token_data = query.first()
        access_token = token_data.get('accessToken')  # 百度统计 Access Token
        params['access_token'] = access_token

    url = 'https://openapi.baidu.com/rest/2.0/tongji/report/getData?'
    req = requests.get(url=url, data=params)
    return req.json()


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        params = dict(parse.parse_qsl(urlparse(self.path).query))
        data = get_data(params)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return
