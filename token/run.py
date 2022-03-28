# -*- coding: utf-8 -*-
# @Author   : Eurkon
# @Date     : 2022/3/28 15:21

import os
import leancloud
import requests


class UpdateAccessToken:
    def __init__(self):
        self.api_key = os.environ["APIKEY"]  # 百度 API Key
        self.secret_key = os.environ["SECRETKEY"]  # 百度 Secret Key
        self.access_token = ''  # 百度统计 Access Token
        self.refresh_token = ''  # 百度统计 Refresh Token
        leancloud.init(os.environ["APPID"], os.environ["APPKEY"])
        self.token = leancloud.Object.extend('BaiduToken').query

    def get_token(self):
        self.token.select('accessToken', 'refreshToken')
        token_data = self.token.first()
        self.access_token = token_data.get('accessToken')
        self.refresh_token = token_data.get('refreshToken')

    def update_token(self):
        url = 'http://openapi.baidu.com/oauth/2.0/token?grant_type=refresh_token&refresh_token=' + self.refresh_token + 'client_id=' + self.api_key + '&client_secret=' + self.secret_key
        response = requests.get(url)
        result = response.json()
        print(result)
        self.access_token = result['access_token']
        self.refresh_token = result['refresh_token']
        self.token.set('accessToken', self.access_token)
        self.token.set('refreshToken', self.refresh_token)
        self.token.save()


if __name__ == '__main__':
    u = UpdateAccessToken()
    u.get_token()
    u.update_token()
