# -*- coding: UTF-8 -*-

import json
import requests
from http.server import BaseHTTPRequestHandler
from dateutil.relativedelta import relativedelta
from datetime import datetime

def getdata():
    site_id = "16265874"
    access_token = "121.777f81bf1db4cc8da3aee9337969b587.YQiJGmUJsP4SLUC4R956Igis_O0hzsiCsfT91Yp.wA6FeA"
    end_date = datetime.now().strftime("%Y-%m-%d")
    year_ago = datetime.now() - relativedelta(years=1)
    start = datetime.now() - relativedelta(years=1,days=(5-year_ago.weekday()))
    start_date = start.strftime("%Y-%m-%d")
    url = r"https://openapi.baidu.com/rest/2.0/tongji/report/getData?access_token=" + access_token + "&site_id=" + site_id + "&start_date=" + start_date + "&end_date=" + end_date + "&metrics=pv_count&method=overview%2FgetTimeTrendRpt"
    req = requests.get(url)
    return req.text

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = getdata()
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return
