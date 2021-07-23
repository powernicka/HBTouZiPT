# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     insert
   Description :
   Author :       gyl
   date：          2021/7/20
-------------------------------------------------
   Change Activity:
                   2021/7/20:
-------------------------------------------------
"""
__author__ = 'gyl'

import time

import pyodbc


def insert(sql):
    try:
        driver = 'SQL Server Native Client 11.0'  # 因版本不同而异
        server = '.'
        user = 'sa'
        password = '1'
        database = '河北邯郸招标投标平台'

        connect = pyodbc.connect(driver=driver, server=server, user=user, password=password, database=database)

        cur = connect.cursor()
        cur.execute(sql)
        time.sleep(0.1)
    except Exception as error:
        connect.rollback()
        print("数据插入失败!" + error)
    cur.close()
    connect.close()