import os

#application配置参数
settings = dict(
    static_path = os.path.join(os.path.dirname(__file__),"static"),
    cookie_secret = "",
    xsrf_cookies = True,
    debug = True
)

#redis配置参数
redis_options = dict(
    host = "127.0.0.1",
    port = 6379
)

#日志配置
log_path = os.path.join(os.path.dirname(__file__),"logs/log")
log_level = "debug"

# 密码加密密钥
passwd_hash_key = "nlgCjaTXQX2jpupQFQLoQo5N4OkEmkeHsHD9+BBx2WQ="

#数据库配置
mysql_conf = dict(
            host="localhost",
            port=3306,
            database="ihome",
            user="root",
            password="root",
            charset="utf8"
)