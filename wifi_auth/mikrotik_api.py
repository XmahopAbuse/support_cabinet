import routeros_api  # библиотека для работы с микротиком по телнету
import json
from hurry.filesize import size  # conver bytes into mb
import os
import pymysql


class RouterOSData:

    def __init__(self, ip_address, login, password):
        self.connection = routeros_api.RouterOsApiPool(ip_address, username=login,
                                                       password=password)
        self.api = self.connection.get_api()

    def get_active_users(self):
        query_active_users = self.api.get_resource('/ip/hotspot/active')
        get_active_user = query_active_users.get()
        data = []
        for elem in get_active_user:
            data.append({'user': elem['user'],
                         'mac-address': elem['mac-address'],
                         'uptime': elem['uptime'],
                         'bytes-in': size(int(elem['bytes-in'])),
                         'bytes-out': size(int(elem['bytes-out'])),

                         })
        return (json.dumps(data))

    def get_cookies(self):
        query_get_cookies = self.api.get_resource('/ip/hotspot/cookie')
        get_cookies = query_get_cookies.get()
        data = []
        for elem in get_cookies:
            data.append({'user': elem['user'],
                         'mac-address': elem['mac-address'],
                         'expires-in': elem['expires-in']})
        return json.dumps(data)


class Mysql_connect():

    def __init__(self, ip_address, login, password, basename):
        self.con = pymysql.connect(ip_address, login, password, basename)

    def get_users_from_base(self):
        with self.con:
            cur = self.con.cursor()
            cur.execute(
                'SELECT username,value,mac,location_name FROM radcheck ORDER BY `id` DESC limit 3')
            rows = cur.fetchall()
            users_json = []
            for row in rows:
                print(row)
                users_json.append({"number": row[0],
                                   "password": row[1],
                                   "mac": row[2],
                                   "location_name": row[3]})
            return (json.dumps(users_json))




