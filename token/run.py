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
        self.app_id = os.environ["APPID"]  # LeanCloud AppID
        self.app_key = os.environ["APPKEY"]  # LeanCloud AppKey

        leancloud.init(self.app_id, self.app_key)
        self.token = leancloud.Object.extend('BaiduToken')
        self.query = self.token.query

    def get_token(self):
        self.query.select('accessToken', 'refreshToken')
        token_data = self.query.first()
        self.object_id = token_data.get('objectId')  # LeanCloud ID
        self.access_token = token_data.get('accessToken')  # 百度统计 Access Token
        self.refresh_token = token_data.get('refreshToken')  # 百度统计 Refresh Token

    def update_token(self):
        url = 'http://openapi.baidu.com/oauth/2.0/token?grant_type=refresh_token&refresh_token=' \
              + self.refresh_token + '&client_id=' + self.api_key + '&client_secret=' + self.secret_key
        response = requests.get(url)
        result = response.json()
        try:
            self.access_token = result['access_token']
            self.refresh_token = result['refresh_token']
            delete = self.token.create_without_data(self.object_id)
            delete.destroy()
            save = self.token()
            save.set('accessToken', self.access_token)
            save.set('refreshToken', self.refresh_token)
            save.save()
        except:
            pass


if __name__ == '__main__':
    u = UpdateAccessToken()
    u.get_token()
    u.update_token()
