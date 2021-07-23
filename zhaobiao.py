# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     zhaobiao
   Description :
   Author :       gyl
   date：          2021/7/14
-------------------------------------------------
   Change Activity:
                   2021/7/14:
-------------------------------------------------
"""
__author__ = 'gyl'

import datetime
from io import BytesIO

import pyodbc
import re
# import pytesseract
# from PIL import Image
import requests
import bs4
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from insert import insert
from 平台内 import PT

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '103',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'JSESSIONID=AD13E580AAC8383911935D8C8E58BFAE; __51cke__=; __tins__19687679=%7B%22sid%22%3A%201626922236318%2C%20%22vd%22%3A%203%2C%20%22expires%22%3A%201626924047318%7D; __51laig__=3',
    'Host':'www.hebeieb.com',
    'Origin': 'http://www.hebeieb.com',
    'Pragma': 'no-cache',
    'Referer': 'http://www.hebeieb.com/tender/xxgk/list.do?selectype=zbgg',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

headers1 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '81',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': '__51cke__=; JSESSIONID=F992D4CF00F5761DED99A77E9B6585A0; __tins__19687679=%7B%22sid%22%3A%201626316947885%2C%20%22vd%22%3A%2011%2C%20%22expires%22%3A%201626319487305%7D; __51laig__=14',
    'Host':'www.hebeieb.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',

}
# headers2 = {
#     'Referer': 'http://www.hebeieb.com/tender/xxgk/list.do?selectype=zbgg',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
#
# }


# def get_proxy():
#     return requests.get("http://127.0.0.1:5000/get/").json()
#
#
# def delete_proxy(proxy):
#     requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))
#
# proxy = get_proxy().get("proxy")

def get_html(url,fordata):

     html = requests.post(url,headers=headers,  data=fordata,timeout=50)
     if html.status_code == 200:
         print('页面获取成功')
         # print(html.text)
         parse_html(html.text)
         time.sleep(1)
         html.close()
     else:
         print('ERROR',html.status_code)
         html.close()
     return

def parse_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    classs = soup.find_all('div',class_='publicont')
    i=1
    for calss in classs:
            print('*' * 15 + '本页第' + str(i) + '个开始导入' + '*' * 15)
            contents= calss.contents[1].text
            #
            content = contents.split('\n')
            href = calss.find('a')['href']
            infoid = href.split('&')[1].split('=')[1]
            if content[9]!='[平台内]':

                url1 = 'http://www.hebeieb.com/infogk/newDetail.do?categoryid=101101&infoid='+infoid+'&jypt=jypt'

                html1 = requests.get(url1, headers=headers1,timeout=50)
                time.sleep(1)
                if html1.status_code == 200:
                    # print('点击页面获取成功')
                    soup1 = bs4.BeautifulSoup( html1.text, 'html.parser')
                    tables = soup1.find(id="article_con").contents[1]
                    number = infoid
                    mainbody = tables.contents[1].contents[7]
                    fullsql = " insert into [dbo].[招标公告] VALUES ('"+content[2].split('. ')[1]+"','"+content[7]+"','"+content[9]+"','"+content[11]+"','"+content[13]+"','"+number+"','"+mainbody.text+"','"+content[3]+"','null','"+   url1+"','"+datetime.datetime.now().strftime('%Y-%m-%d')+"');commit;"
                    insert(fullsql)
                    print('*'*10+'招标公告完成'+'*'*10)
                else:
                    print('ERROR', html.status_code)
                    html.close()
            else:

                PT(infoid,content)
            print('*'*15+'本页第'+str(i)+'个完成'+'*'*15)
            i += 1





if __name__ == '__main__':
    url = 'http://www.hebeieb.com/tender/xxgk/zbgg.do'

    for i in range(86,175):
        fordata = {
            'page':i,
            'TimeStr':'2020-01-01,2020-12-31',
            'allDq': '130400',
            'allHy': 'reset1',
            'AllPtName':'',
            'KeyStr':'',
            'KeyType': 'ggname'
        }
        print('*'*30+'正在爬取第{}页'.format(i)+'*'*30)
        try:
            # url1 = url.format(i)
            get_html(url,fordata)
            print('*'*30+'第{}页爬取成功'.format(i)+'*'*30)
        except Exception as error:
            print('*'*20+"第{}页爬取失败!".format(i) + error+'*'*20)
        time.sleep(2)