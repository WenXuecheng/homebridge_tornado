import os
BASE_DIRS = os.path.dirname(__file__)

#参数
options = {
    "port": 6526
}

#数据库配置
mysql = {
    "host": "10.0.144.21",
    "user": "root",
    "passwd": "sunck",
    "dbName": "test"
}

#配置
settings = {
    "static_path": os.path.join(BASE_DIRS, "static"),
    "template_path": os.path.join(BASE_DIRS, "templates"),
    "wifi_dev_path": os.path.join(BASE_DIRS, "wifi_dev"),
    "views_path": os.path.join(BASE_DIRS, "views"),
    "debug": True
}

