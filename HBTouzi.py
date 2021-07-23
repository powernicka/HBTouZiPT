from io import BytesIO

import pyodbc
# import pytesseract
# from PIL import Image
import requests
import bs4
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from insert import insert

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
    'Cookie': 'Hm_lvt_82698a74ed862e6a03fc9e4cbac594a6=1617780782; Hm_lvt_727d5904b141f326c9cb1ede703d1162=1617780782; access_token=cn-6494d550-a79c-4560-bf98-3c489fe44775; _ga=GA1.2.208285359.1617780860; _gid=GA1.2.424844335.1617780860; location_code=340000; gldjc_sessionid=7ff53203-fa02-4175-ab81-af3d46b2e801; loginUuid=7ff53203-fa02-4175-ab81-af3d46b2e801; Hm_lpvt_82698a74ed862e6a03fc9e4cbac594a6=1617842029; Hm_lpvt_727d5904b141f326c9cb1ede703d1162=1617842029'
}

headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
    'Cookie': 'theme=indigo; size=13; JSESSIONID=6508098E94138DA9CC26075E5B657AF3; CheckCode=7795',
    'Referer': 'http://tzxm.hbzwfw.gov.cn/sbglweb/gsxxList'
}


def get_proxy():
    return requests.get("http://127.0.0.1:5000/get/").json()


def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

proxy = get_proxy().get("proxy")

def get_html(url,fordata):

     html = requests.post(url,headers=headers, proxies={"http": "http://{}".format(proxy)}, data=fordata,timeout=50)
     if html.status_code == 200:
         print('页面获取成功')
         # print(html.text)
         parse_html(html.text)
         html.close()
     else:
         print('ERROR',html.status_code)
         html.close()
     return


def parse_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    trs = soup.select('tr')
    for tr in trs[3:]:
                a = tr.contents[3].contents[1].attrs['href']
                id = a[23:47]
                href = a[50:-3]
                url1 = 'http://tzxm.hbzwfw.gov.cn/sbglweb/xminfo?xmdm='+id+'&sxid='+href+'&xzqh=130000'

                html1 = requests.get(url1, headers=headers1,proxies={"http": "http://{}".format(proxy)}, timeout=50)
                if html1.status_code == 200:
                    # print('点击页面获取成功')
                    html1 = html1.text
                    soup1 = bs4.BeautifulSoup(html1, 'html.parser')
                    tables = soup1.select('td')
                    j = 3
                    k = 3
                    sql = ''
                    sql1 = ''
                    sql2 = ''
                    for table  in  tables[3:]:
                        if j%2 ==1 and  j<10 :
                            # print(table.text)
                            sql = sql + "N'"+table.text.replace("\r\n",'').replace("\t",'').replace(u'\xa0','')+"',"
                        if  j > 16 and  j <22:
                            # print(table.text)
                            sql1 = sql1 + "N'"+table.text.replace("\r\n",'').replace("\t",'').replace(u'\xa0','')+"',"
                            if k == 21:
                                fullsql = " insert into [dbo].[邯郸投资平台数据_Crawler] VALUES ("+sql+sql1[:-1]+');commit;'
                                insert(fullsql)
                        if  j > 28:
                            # print(table.text)
                            sql2 = sql2 + "N'" + table.text.replace("\r\n",'').replace("\t",'').replace(u'\xa0','') + "',"
                            if  k==33 or k==38 or k==43 or k==48 or k==53 or k==58 or k==63   or k==68 or k==73 or k==78 or k==83 or k==88 or k==93:
                                fullsql1 = " insert into [dbo].[邯郸投资平台数据_Crawler] VALUES (" + sql + sql2[:-1] + ');commit;'
                                insert(fullsql1)
                                sql2 = ''
                        j+=1
                        k+=1
                else:
                    print('ERROR', html.status_code)
                    html.close()


if __name__ == '__main__':
    url = 'http://tzxm.hbzwfw.gov.cn/sbglweb/gsxxList'

    for i in range(1,100):
        fordata = {
            'xzqh': '130400',
            'rows': '25',
            'page': i
        }
        print('正在爬取第{}页'.format(i))
        try:
            # url1 = url.format(i)
            get_html(url,fordata)
            print('第{}页爬取成功'.format(i))
        except Exception as error:
            print("第{}页爬取成功!".format(i) + error)
        time.sleep(2)