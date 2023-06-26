# baidu-tongji-api
使用python获取百度统计数据，解决跨域请求的问题，部署在vercel的api

# 教程文章
https://blog.eurkon.com/post/61763977.html

# 若 token 过期则需手动更新 LeanCloud 存储的 token

http://openapi.baidu.com/oauth/2.0/authorize?response_type=code&client_id={CLIENT_ID}&redirect_uri=oob&scope=basic&display=popup

http://openapi.baidu.com/oauth/2.0/token?grant_type=authorization_code&code={CODE}&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&redirect_uri=oob
