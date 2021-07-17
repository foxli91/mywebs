import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='root', password='rBCL2HO6Onn27yl3', charset='utf8'
                       , database='my_py_webs')


def get_cursor():
    # 开启连接
    conn.connect()
    # 设置对应的字典项
    return conn.cursor(cursor=pymysql.cursors.DictCursor)


def close_conn():
    conn.close()
