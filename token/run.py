# -*- coding: utf-8 -*-
# @Author   : Eurkon
# @Date     : 2022/3/28 16:23

from token.UpdateAccessToken import UpdateAccessToken

if __name__ == '__main__':
    u = UpdateAccessToken()
    u.get_token()
    u.update_token()
