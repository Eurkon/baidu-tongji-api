# -*- coding: UTF-8 -*-

import json
import requests
from http.server import BaseHTTPRequestHandler
from dateutil.relativedelta import relativedelta
from datetime import datetime
from urlparse import parse_qs


def getdata(site_id, access_token):
    end_date = datetime.now().strftime('%Y-%m-%d')
    year_ago = datetime.now() - relativedelta(years=1)
    start = datetime.now() - relativedelta(years=1, days=(5 - year_ago.weekday()))
    start_date = start.strftime('%Y-%m-%d')
    url = r'https://openapi.baidu.com/rest/2.0/tongji/report/getData?access_token=' + access_token + '&site_id=' + site_id + '&start_date=' + start_date + '&end_date=' + end_date + '&metrics=pv_count&method=overview%2FgetTimeTrendRpt'
    req = requests.get(url)
    return req.text


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        param = parse_qs(path.split('?')[1])
        data = getdata(param['id'], param['token'])
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return
