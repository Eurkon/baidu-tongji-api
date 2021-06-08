# -*- coding: UTF-8 -*-

import json
import requests
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs


def get_data(params):
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
