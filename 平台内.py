# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :
   Author :       gyl
   date：          2021/7/20
-------------------------------------------------
   Change Activity:
                   2021/7/20:
-------------------------------------------------
"""
__author__ = 'gyl'

import datetime
import json
import re

import bs4
import requests
from lxml import  etree

from insert import insert

def  PT(infoid,content):
    bdcodes = infoid
    url = 'http://www.hebeieb.com/infogk/detail.do?categoryid=101101&infoid='+infoid+'&bdcodes='+infoid+'&laiyuan=%255B%25E5%25B9%25B3%25E5%258F%25B0%25E5%2586%2585%255D'
    headers = {
    'Host': 'www.hebeieb.com',
    'Origin': 'http://www.hebeieb.com',
    'Pragma': 'no-cache',
    'Referer': url,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    }
    headers1 = {
        'Host': 'www.hebeieb.com',
        'Referer': 'http://www.hebeieb.com/tender/xxgk/list.do?selectype=zbgg',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    }
    res=requests.get(url,headers = headers1,timeout=50)
    res.encoding='utf-8'
    # print(res.text)
    load = re.findall(r'\$\(".time_zhou"\).eq\(0\).append\(creatTimeLine\((.*?)\]',res.text)
    jsona = json.loads(load[0]+']')
    for jsonb in jsona:
        categoryid = jsonb['categoryid']
        infoid = jsonb['infoid']
        lx = jsonb['lx']
        url1 = 'http://www.hebeieb.com/infogk/newDetail.do?categoryid=' + categoryid + '&infoid=' + infoid + '&laiyuan=[%E5%B9%B3%E5%8F%B0%E5%86%85]'
        fordata = {
            'categoryid': categoryid,
            'infoid': infoid,
            'laiyuan': '[平台内]',
        }
        html = requests.post(url1, headers=headers, data=fordata, timeout=50)
        soup = etree.HTML(html.content.decode('utf-8'))
        soup1 = bs4.BeautifulSoup(html.text, 'html.parser')

        招标公告编号 = bdcodes

        if categoryid =='101101' and lx=='招标公告' :
            fullsql = " insert into [dbo].[招标公告] VALUES ('" + content[2].split('. ')[1] + "','" + content[7] + "','" +content[9] + "','" + content[11] + "','" + content[13] + "','" + bdcodes + "','" + soup1.text + "','" + jsonb['wjhqtime'] + "','" + jsonb['wjdjjztime']+ "','" + url1 + "','" + datetime.datetime.now().strftime('%Y-%m-%d') + "');commit;"
            insert(fullsql)
            print('*'*10+'招标公告完成'+'*'*10)

        if categoryid == '101102' and lx=='开标记录':
            标段 = soup.xpath('//*[@id="article_con"]/div/table/tr[2]/td/table/tbody/tr[2]/td/text()')[0]
            开标时间 = soup.xpath('//*[@id="article_con"]/div/table/tr[2]/td/table/tbody/tr[4]/td[1]/text()')[0]
            开标地点 = soup.xpath('//*[@id="article_con"]/div/table/tr[2]/td/table/tbody/tr[4]/td[2]/text()')[0]
            trs = soup1.find_all('tr', attrs={'ng-repeat': 'x in mxlist'})
            for tr in trs:
                序号 = tr.contents[1].text
                投标单位名称 = tr.contents[3].text
                统一社会信用代码 = tr.contents[5].text
                工期 = tr.contents[7].text
                投标报价 = tr.contents[9].text
                投标文件递交时间 = tr.contents[11].text
                项目负责人 = tr.contents[12].text
                质量标准 = tr.contents[13].text
                其他内容 = tr.contents[14].text
                fullsql = " insert into [dbo].[开标记录] VALUES ('" + 标段 + "','" + 开标时间 + "','" + 开标地点 + "','" + 序号 + "','" + 投标单位名称 + "','" + 统一社会信用代码 + "','" + 工期 + "','" + 投标报价 + "','" + 投标文件递交时间 + "','" + 项目负责人 + "','" + 质量标准 + "','" + 其他内容 + "','" + 招标公告编号 + "');commit;"
                insert(fullsql)
            print('*'*10+'开标记录完成'+'*'*10)

        if  categoryid =='BgGg' or (categoryid =='101102' and lx=='变更公示') or (categoryid =='101103' and lx=='变更公示') or (categoryid =='101104' and lx=='变更公示'):

            变更标题 =  soup.xpath('//*[@id="article_con"]/div/table/tr[1]/th/h2/text()')[0]
            fullsql = " insert into [dbo].[变更公告] VALUES ('" + 变更标题 + "','" + soup1.text + "','" + bdcodes +"','" + lx + "');commit;"
            insert(fullsql)
            print('*'*10+'变更公告完成'+'*'*10)

        if categoryid =='101103' and lx=='中标候选人公示' :
            标段 = soup.xpath('//*[@id="article_con"]/div/table/tr[2]/td/table/tbody/tr[2]/td/text()')[0]
            所属行业 = soup.xpath('//*[@id="article_con"]/div/table/tr[2]/td/table/tbody/tr[3]/td[1]/text()')[0]
            所属地区 = soup.xpath('//*[@id="article_con"]/div/table/tr[2]/td/table/tbody/tr[3]/td[2]/text()')[0]
            开标时间 = soup.xpath('//*[@id="article_con"]/div/table/tr[2]/td/table/tbody/tr[4]/td[1]/text()')[0]
            开标地点 = soup.xpath('//*[@id="article_con"]/div/table/tr[2]/td/table/tbody/tr[4]/td[2]/text()')[0]
            公示开始日期 = soup.xpath('//*[@id="article_con"]/div/table/tr[2]/td/table/tbody/tr[5]/td[1]/text()')[0]
            公示截止日期 = soup.xpath('//*[@id="article_con"]/div/table/tr[2]/td/table/tbody/tr[5]/td[2]/text()')[0]

            排名 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[3]/td[1]/div/text()')[0]
            统一社会信用代码 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[3]/td[2]/div/text()')[0]
            中标候选人单位名称 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[3]/td[3]/div/text()')[0]
            投标价格 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[3]/td[4]/div/text()')[0]
            评标价格 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[3]/td[5]/div/text()')[0]
            try:
                评分结果 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[3]/td[6]/div/text()')[0]
            except IndexError:
                评分结果=''

            质量标准 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[3]/td[7]/div/text()')[0]
            工期 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[3]/td[8]/div/text()')[0]
            try:
                备注 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[last()]/td/text()')[0]
            except IndexError:
                备注=''
            try:
                职务 = soup.xpath('//*[@id="article_con"]/div/table/tr[4]/td/table/tbody/tr[3]/td[1]/text()')[0]
            except IndexError:
                职务 = ''
            try:
                姓名 = soup.xpath('//*[@id="article_con"]/div/table/tr[4]/td/table/tbody/tr[3]/td[2]/text()')[0]
            except IndexError:
                姓名 = ''
            try:
                职称 = soup.xpath('//*[@id="article_con"]/div/table/tr[4]/td/table/tbody/tr[3]/td[3]/text()')[0]
            except IndexError:
                职称 = ''
            try:
                执业或职业资格 = soup.xpath('//*[@id="article_con"]/div/table/tr[4]/td/table/tbody/tr[3]/td[4]/text()')[0]
            except IndexError:
                执业或职业资格 = ''
            try:
                执业或职业资格 = soup.xpath('//*[@id="article_con"]/div/table/tr[4]/td/table/tbody/tr[3]/td[4]/text()')[0]
            except IndexError:
                执业或职业资格 = ''
            try:
                证书编号 = soup.xpath('//*[@id="article_con"]/div/table/tr[4]/td/table/tbody/tr[3]/td[5]/text()')[0]
            except IndexError:
                证书编号 = ''
            try:
                响应招标文件要求的资格能力条件  = soup.xpath('//*[@id="article_con"]/div/table/tr[4]/td/table/tbody/tr[5]/td/text()')[0]
            except IndexError:
                响应招标文件要求的资格能力条件 = ''


            招标人 = soup.xpath('//*[@id="article_con"]/div/table/tr[last()]/td/table/tbody/tr[2]/td[1]/text()')[0]
            招标人联系人 = soup.xpath('//*[@id="article_con"]/div/table/tr[last()]/td/table/tbody/tr[3]/td[1]/text()')[0]
            招标人地址 = soup.xpath('//*[@id="article_con"]/div/table/tr[last()]/td/table/tbody/tr[4]/td[1]/text()')[0]
            招标人电话 = soup.xpath('//*[@id="article_con"]/div/table/tr[last()]/td/table/tbody/tr[5]/td[1]/text()')[0]
            招标人电子邮箱 = soup.xpath('//*[@id="article_con"]/div/table/tr[last()]/td/table/tbody/tr[6]/td[1]/text()')[0]
            招标代理机构 = soup.xpath('//*[@id="article_con"]/div/table/tr[last()]/td/table/tbody/tr[2]/td[2]/text()')[0]
            招标代理联系人 = soup.xpath('//*[@id="article_con"]/div/table/tr[last()]/td/table/tbody/tr[3]/td[2]/text()')[0]
            招标代理地址 = soup.xpath('//*[@id="article_con"]/div/table/tr[last()]/td/table/tbody/tr[4]/td[2]/text()')[0]
            招标代理电话 = soup.xpath('//*[@id="article_con"]/div/table/tr[last()]/td/table/tbody/tr[5]/td[2]/text()')[0]
            招标代理电子邮箱 = soup.xpath('//*[@id="article_con"]/div/table/tr[last()]/td/table/tbody/tr[6]/td[2]/text()')[0]

            fullsql = " insert into [dbo].[中标候选人公示] VALUES ('"+标段+"','"+所属行业+"','"+所属地区+"','"+开标时间+"','"+开标地点+"','"+公示开始日期+"','"+公示截止日期+"','"+排名+"','"+统一社会信用代码+"','"+中标候选人单位名称+"','"+投标价格.replace('\r\n','').strip()+"','"+评标价格.replace('\r\n','').strip()+"','"+评分结果+"','"+质量标准+"','"+工期+"','"+备注+"','"+职务+"','"+姓名+"','"+职称+"','"+执业或职业资格+"','"+证书编号+"','"+响应招标文件要求的资格能力条件+"','"+招标人+"','"+招标人联系人+"','"+招标人地址+"','"+招标人电话+"','"+招标人电子邮箱+"','"+招标代理机构+"','"+招标代理联系人+"','"+招标代理地址+"','"+招标代理电话+"','"+招标代理电子邮箱+"','"+招标公告编号+"');commit;"
            insert(fullsql)

            try:
                排名 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[4]/td[1]/div/text()')[0]
                统一社会信用代码 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[4]/td[2]/div/text()')[0]
                中标候选人单位名称 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[4]/td[3]/div/text()')[0]
                投标价格 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[4]/td[4]/div/text()')[0]
                评标价格 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[4]/td[5]/div/text()')[0]
                try:
                    评分结果 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[4]/td[6]/div/text()')[0]
                except IndexError:
                    评分结果 = ''

                质量标准 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[4]/td[7]/div/text()')[0]
                工期 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[4]/td[8]/div/text()')[0]
                try:
                    职务 = soup.xpath('//*[@id="article_con"]/div/table/tr[5]/td/table/tbody/tr[3]/td[1]/text()')[0]
                except IndexError:
                    职务 = ''
                try:
                    姓名 = soup.xpath('//*[@id="article_con"]/div/table/tr[5]/td/table/tbody/tr[3]/td[2]/text()')[0]
                except IndexError:
                    姓名 = ''
                try:
                    职称 = soup.xpath('//*[@id="article_con"]/div/table/tr[5]/td/table/tbody/tr[3]/td[3]/text()')[0]
                except IndexError:
                    职称 = ''
                try:
                    执业或职业资格 = soup.xpath('//*[@id="article_con"]/div/table/tr[5]/td/table/tbody/tr[3]/td[4]/text()')[0]
                except IndexError:
                    执业或职业资格 = ''
                try:
                    执业或职业资格 = soup.xpath('//*[@id="article_con"]/div/table/tr[5]/td/table/tbody/tr[3]/td[4]/text()')[0]
                except IndexError:
                    执业或职业资格 = ''
                try:
                    证书编号 = soup.xpath('//*[@id="article_con"]/div/table/tr[5]/td/table/tbody/tr[3]/td[5]/text()')[0]
                except IndexError:
                    证书编号 = ''
                try:
                    响应招标文件要求的资格能力条件 = \
                    soup.xpath('//*[@id="article_con"]/div/table/tr[5]/td/table/tbody/tr[5]/td/text()')[0]
                except IndexError:
                    响应招标文件要求的资格能力条件 = ''

                fullsql = " insert into [dbo].[中标候选人公示] VALUES ('"+标段+"','"+所属行业+"','"+所属地区+"','"+开标时间+"','"+开标地点+"','"+公示开始日期+"','"+公示截止日期+"','"+排名+"','"+统一社会信用代码+"','"+中标候选人单位名称+"','"+投标价格.replace('\r\n','').strip()+"','"+评标价格.replace('\r\n','').strip()+"','"+评分结果+"','"+质量标准+"','"+工期+"','"+备注+"','"+职务+"','"+姓名+"','"+职称+"','"+执业或职业资格+"','"+证书编号+"','"+响应招标文件要求的资格能力条件+"','"+招标人+"','"+招标人联系人+"','"+招标人地址+"','"+招标人电话+"','"+招标人电子邮箱+"','"+招标代理机构+"','"+招标代理联系人+"','"+招标代理地址+"','"+招标代理电话+"','"+招标代理电子邮箱+"','"+招标公告编号+"');commit;"
                insert(fullsql)
            except IndexError:
                pass

            try:
                排名 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[5]/td[1]/div/text()')[0]
                统一社会信用代码 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[5]/td[2]/div/text()')[0]
                中标候选人单位名称 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[5]/td[3]/div/text()')[0]
                投标价格 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[5]/td[4]/div/text()')[0]
                评标价格 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[5]/td[5]/div/text()')[0]
                try:
                    评分结果 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[5]/td[6]/div/text()')[0]
                except IndexError:
                    评分结果 = ''

                质量标准 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[5]/td[7]/div/text()')[0]
                工期 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[5]/td[8]/div/text()')[0]
                try:
                    职务 = soup.xpath('//*[@id="article_con"]/div/table/tr[6]/td/table/tbody/tr[3]/td[1]/text()')[0]
                except IndexError:
                    职务 = ''
                try:
                    姓名 = soup.xpath('//*[@id="article_con"]/div/table/tr[6]/td/table/tbody/tr[3]/td[2]/text()')[0]
                except IndexError:
                    姓名 = ''
                try:
                    职称 = soup.xpath('//*[@id="article_con"]/div/table/tr[6]/td/table/tbody/tr[3]/td[3]/text()')[0]
                except IndexError:
                    职称 = ''
                try:
                    执业或职业资格 = soup.xpath('//*[@id="article_con"]/div/table/tr[6]/td/table/tbody/tr[3]/td[4]/text()')[0]
                except IndexError:
                    执业或职业资格 = ''
                try:
                    执业或职业资格 = soup.xpath('//*[@id="article_con"]/div/table/tr[6]/td/table/tbody/tr[3]/td[4]/text()')[0]
                except IndexError:
                    执业或职业资格 = ''
                try:
                    证书编号 = soup.xpath('//*[@id="article_con"]/div/table/tr[6]/td/table/tbody/tr[3]/td[5]/text()')[0]
                except IndexError:
                    证书编号 = ''
                try:
                    响应招标文件要求的资格能力条件 = \
                    soup.xpath('//*[@id="article_con"]/div/table/tr[6]/td/table/tbody/tr[5]/td/text()')[0]
                except IndexError:
                    响应招标文件要求的资格能力条件 = ''

                fullsql = " insert into [dbo].[中标候选人公示] VALUES ('"+标段+"','"+所属行业+"','"+所属地区+"','"+开标时间+"','"+开标地点+"','"+公示开始日期+"','"+公示截止日期+"','"+排名+"','"+统一社会信用代码+"','"+中标候选人单位名称+"','"+投标价格.replace('\r\n','').strip()+"','"+评标价格.replace('\r\n','').strip()+"','"+评分结果+"','"+质量标准+"','"+工期+"','"+备注+"','"+职务+"','"+姓名+"','"+职称+"','"+执业或职业资格+"','"+证书编号+"','"+响应招标文件要求的资格能力条件+"','"+招标人+"','"+招标人联系人+"','"+招标人地址+"','"+招标人电话+"','"+招标人电子邮箱+"','"+招标代理机构+"','"+招标代理联系人+"','"+招标代理地址+"','"+招标代理电话+"','"+招标代理电子邮箱+"','"+招标公告编号+"');commit;"
                insert(fullsql)
            except IndexError:
                pass

            print('*'*10+'中标候选人公示完成'+'*'*10)

        if categoryid =='101104' and lx=='中标结果公示':


            标段 = soup.xpath('//*[@id="article_con"]/div/table/tr[2]/td/table/tbody/tr[2]/td/text()')[0]
            公示发布日期 = soup.xpath('//*[@id="article_con"]/div/table/tr[2]/td/table/tbody/tr[4]/td[2]/text()')[0]
            排名 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[3]/td[1]/div/text()')[0]
            统一社会信用代码 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[3]/td[2]/div/text()')[0]
            中标候选人单位名称 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[3]/td[3]/div/text()')[0]
            投标价格 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[3]/td[4]/text()')[0]
            大写中标价格 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[3]/td[5]/text()')[0]
            质量标准 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[3]/td[6]/div/text()')[0]
            工期  = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[3]/td[7]/div/text()')[0]
            try:
                其它公示内容 = soup.xpath('//*[@id="article_con"]/div/table/tr[3]/td/table/tbody/tr[4]/td/text()')[0]
            except IndexError:
                其它公示内容=''

            # print(标段,公示发布日期,排名,统一社会信用代码,中标候选人单位名称,投标价格.replace('\r\n','').strip(),大写中标价格.replace('\r\n','').strip(),质量标准,工期,其它公示内容,招标公告编号)
            fullsql = " insert into [dbo].[中标结果公示] VALUES ('"+标段+"','"+公示发布日期+"','"+排名+"','"+统一社会信用代码+"','"+中标候选人单位名称+"','"+投标价格.replace('\r\n','').strip()+"','"+大写中标价格.replace('\r\n','').strip()+"','"+质量标准+"','"+工期+"','"+其它公示内容+"','"+招标公告编号+"');commit;"
            insert(fullsql)
            print('*'*10+'中标结果公示完成'+'*'*10)
