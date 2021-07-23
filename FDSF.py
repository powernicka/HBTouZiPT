# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     FDSF
   Description :
   Author :       gyl
   date：          2021/7/22
-------------------------------------------------
   Change Activity:
                   2021/7/22:
-------------------------------------------------
"""
__author__ = 'gyl'

import bs4

html = '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

    <html>

    <head>
        <meta name="viewport" content="width=device-width,minimum-scale=1,maximum-scale=1,user-scalable=no" />
        <title>详细内容 - 河北省招标投标公共服务平台</title>
        <meta name="renderer" content="webkit">
<meta http-equiv = "X-UA-Compatible" content = "IE=edge,chrome=1" />
<script src="/resweb/Scripts/jquery-1.7.2.min.js" type="text/javascript"></script>

<script src="/resweb/Scripts/jquery.url.js" type="text/javascript"></script>


<script src="/resweb/Scripts/zzsc.js" type="text/javascript"></script>
<script src="/resweb/Scripts/textScroll.js" type="text/javascript"></script>
<script src="/resweb/Scripts/tab.js" type="text/javascript"></script>

<script src="/res/js/lib/jquery-1.11.0.min.js"></script>
<script src="/res/js/base/bootstrap.min.js" type="text/javascript"></script>

<script src="/res/js/lib/jquery-ui.min.js"></script>

<script src="/res/js/lib/jquery.form.min.js"></script>
<script src="/res/js/app.js"></script>
<script src="/res/layer/layer.js"></script>
<script src="/res/js/rh_common.js" type="text/javascript"></script>
<script src="/res/js/session.js" type="text/javascript"></script>

<link rel="stylesheet" href="/res/css/styles/rh_common.css" type="text/css" />
<link href="/resweb/Content/Dialog/green/css.css" rel="stylesheet" type="text/css" />
 <link rel="stylesheet" href="/res/css/styles/jqueryUI/jquery-ui.css" type="text/css"/>
 
 <link rel="shortcut icon" href="/resweb/Images/logo.ico" />
<link rel="bookmark" href="/resweb/Images/logo.ico" />
<link rel="stylesheet" href="/resweb/Content/Font-Awesome-3.2.1/css/font-awesome.min.css" />
<link rel="stylesheet" href="/resweb/Content/animation.css" />
<link rel="stylesheet" href="/resweb/Content/main.css" />
<link rel="stylesheet" href="/resweb/Content/form.css" />
<link href="/resweb/Content/user_center.css" rel="stylesheet" type="text/css" />
<link rel="stylesheet" href="/resweb/Content/main_new.css" /><meta name="renderer" content="webkit">
<meta http-equiv = "X-UA-Compatible" content = "IE=edge,chrome=1" />
<script src="/res/js/lib/jquery-ui.min.js"></script>
	<script src="/res/js/rh_common.js" type="text/javascript"></script>
	<link rel="stylesheet" type="text/css" href="/resweb/webnew_css/x-style.css"/>
	<link rel="stylesheet" href="/res/css/styles/jqueryUI/jquery-ui.css" type="text/css">


<style>
        .infro_table {
            width: 100%;
            margin-top: 20px;
            /*table-layout: auto;*/
        }

        .infro_table th,
        .infro_table td {
            padding: 5px 10px;
            font-size: 14px;
            word-break: break-all;
            border-color: #ddd
        }
        .infro_table th  {
          width: 160px;
            text-align: center;
            font-size: 14px;
        }
        .infro_table td{white-space:normal; word-break:break-all;}
        p{
            text-indent: 2em;
        }
        table{ width: 100% !important }
        </style>
    </head>

    <body>

 		<div class="x-warp x-m">
				
                <div class="article" id="article_con">
                <div class="article_con" >
                            <table class="infro_table" >

                                        <tr >
                                            
                                            <th colspan="2" style='text-align: center;' ><h2>邯郸市中心医院耳鼻喉科电子鼻咽喉镜采购项目单一来源</h2></th>
                                        </tr> 
                                              <style type="text/css">
                                                 .article_con table{border-collapse:collapse; border-spacing:0; }
                                                    .article_con table,.article_con table th,.article_con table td{ border-color: #ddd;border-width: 1px }
                                                    .thtit{ padding: 0 !important; background: #F3F3F3 }
                                                    .thtit p{ border-left: 5px solid #C9C9C9; }
                                                    .article_con table th, .article_con table td{ font-size: 14px !important }
                                                    .infro_table th, .infro_table td{ padding: 5px; }
                                                </style>
                                             <tr>
                                                   <td colspan="2"> 
                                                    <table style="width:100%;" cellspacing="0" cellpadding="2" bordercolor="#000000" border="1"><tbody>
                                                        <tr><th colspan="4" class="thtit"><p>基本信息</p></th></tr>
                                                         <tr>
                                                            <th style="background-color: #F3F3F3;">标段(包)</th>
                                                            <td colspan="3" >邯郸市中心医院耳鼻喉科电子鼻咽喉镜采购项目单一来源</td>
                                                        </tr> 
                                                       
                                                        <tr>
                                                             <th style="background-color: #F3F3F3;">所属行业：</th>
                                                             <td>卫生和社会工作/卫生</td>
                                                             <th style="background-color: #F3F3F3;">所属地区：</th>
                                                             <td>邯郸市-市辖区</td>
                                                        </tr>
                                                   
                                                        <tr>
                                                             <th style="background-color: #F3F3F3;">开标时间:</th>
                                                             <td >2020-12-31 14:30</td>
                                                             <th style="background-color: #F3F3F3;">开标地点:</th>
                                                             <td>邯郸市丛台区丛台路与广泰街交叉口喆啡酒店六楼会议室</td>
                                                        </tr>
                                                        <tr>
                                                            <th style="background-color: #F3F3F3;">公示开始日期:</th>
                                                            <td >2021-01-04</td>
                                                            <th style="background-color: #F3F3F3;">公示截止日期:</th>
                                                            <td >2021-01-06</td>
                                                        </tr>
                                                      
                                                    </tbody></table>
                                                    </td>
                                                </tr>
                                                
                                           
                                        
                                        <tr>
                                            <td colspan="2">
                                                <table style="width:100%;table-layout:inherit" cellspacing="0" cellpadding="2" bordercolor="#000000" border="1"><tbody>
                                                    <tr><th colspan="8" class="thtit"><p>中标候选人名单</p></th></tr>
                                                    <tr style="background-color: #F3F3F3;">
                                                        <th>排名</th>
                                                        <th>统一社会信用代码</th>
                                                        <th>中标候选人单位名称</th>
                                                        <th>投标价格</th>
                                                        <th>评标价格</th>
                                                        <th>评分结果</th>
                                                        <th>质量标准</th>
                                                        <th>工期/交货期</th>
                                                    </tr>
                                                     <tr>
                                                            <td>
                                                                <div style="width: 28px">1</div>
                                                            </td>
                                                            <td>
                                                                <div style="width: 128px">9113040008269376XT</div>
                                                            </td>
                                                            <td>
                                                                <div style="width: 144px">华润邯郸医药有限公司</div>
                                                            </td>
                                                            <td>
                                                                <div style="width: 80px">
                                                                    1425000元人民币</div>
                                                            </td>
                                                            <td>
                                                                <div style="width: 80px">
                                                                    1425000元人民币</td>
                                                                </div>
                                                            <!--  <td>无</td> -->
                                                             <td>
                                                                <div style="width: 44px">/</div>
                                                            </td>
                                                            <td><div style="width: 125px">合格</div></td>
                                                            <td><div style="width: 70px">30天</div></td>
                                                        </tr>
                                                   <tr>
                                                       <td colspan="8">备注：<br/>
                                                        
                                                             第1中标候选人其他说明：无<br/>
                                                             </td>
                                                   </tr>
                                                   </tbody></table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td colspan="2">
                                                <table style="width:100%;" cellspacing="0" cellpadding="2" bordercolor="#000000" border="1"><tbody>
                                                    
                                                    <tr><th colspan="5" class="thtit"><p>第1中标候选人-项目负责人</p></th></tr>
                                                    <tr style="background-color: #F3F3F3;"><th>职务</th><th>姓名</th><th>职称</th><th>执业或职业资格</th><th>证书编号</th></tr>
                                                     
                                                        <tr><td>销售经理</td>
                                                            <td>张文</td>
                                                            <td>/</td>
                                                            <td>/</td>
                                                            <td>/</td>
                                                        </tr>
                                                    
                                                    <tr><th colspan="5" class="thtit"><p>第1中标候选人-响应招标文件要求的资格能力条件</p></th></tr>

                                                        <tr>
                                                            <td colspan="5">完全符合单一来源采购文件要求，并通过协商小组审查。</td>
                                                        </tr>
                                                    </tbody></table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td colspan="2"> <table style="width:100%;" cellspacing="0" cellpadding="2" bordercolor="#000000" border="1"><tbody>
                                                
                                                 <tr><th colspan="2" class="thtit"><p>否决投标单位及理由</p></th></tr>
                                                 <tr>
                                                      <td colspan="2">无</td>
                                                 </tr>
                                             </tbody></table>
                                            
                                           </td>
                                        </tr>
                                        <tr>
                                          <td colspan="2">  <table style="width:100%;" cellspacing="0" cellpadding="2" bordercolor="#000000" border="1"><tbody>
                                               
                                                <tr><th colspan="2" class="thtit"><p>提出异议渠道和方式</p></th></tr>
                                                <tr>
                                                <td colspan="2">以纸质版形式递交至华睿诚项目管理有限公司，联系人：许荣；电话：18931037275；邮箱：1327091424@qq.com</td>
                                                </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                        </tr>
                                        <tr>
                                             <td colspan="2"><table style="width:100%;" cellspacing="0" cellpadding="2" bordercolor="#000000" border="1"><tbody>
                                
                                                 <tr><th colspan="2" class="thtit"><p>招标文件规定公示的其他内容</p></th></tr>
                                                 <tr>
                                                 <td colspan="2">无</td>
                                                </tr>
                                                </tbody></table>
                                                </td>
                                        </tr>
                                        <tr>
                                           <td colspan="2">  <table style="width:100%;" cellspacing="0" cellpadding="2" bordercolor="#000000" border="1"><tbody>
                                                
                                                <tr><th colspan="2" class="thtit"><p>全部投标单位</p></th></tr>
                                                <tr>
                                                <td colspan="2">华润邯郸医药有限公司、</td>
                                                </tr>
                                                </tbody>
                                            </table>
                                            </td>
                                        </tr>
                                         <tr>
                                                   <td colspan="2"> 
                                                    <table style="width:100%;" cellspacing="0" cellpadding="2" bordercolor="#000000" border="1"><tbody>
                                                        <tr><th colspan="4" class="thtit"><p>联系方式</p></th></tr>

                                                        <tr>
                                                             <th style="background-color: #F3F3F3;">招标人：</th>
                                                             <td>邯郸市中心医院</td>
                                                             <th style="background-color: #F3F3F3;">招标代理机构：</th>
                                                             <td>华睿诚项目管理有限公司</td>
                                                        </tr>
                                                         <tr>
                                                            <th style="background-color: #F3F3F3;">联系人:</th>
                                                            <td >李主任</td>
                                                            <th style="background-color: #F3F3F3;">联系人:</th>
                                                            <td >许荣</td>
                                                        </tr>
                                                         <tr>
                                                            <th style="background-color: #F3F3F3;">地址:</th>
                                                            <td >邯郸市丛台北路59号</td>
                                                            <th style="background-color: #F3F3F3;">地址:</th>
                                                            <td >邯郸市联纺东路盛海蓝郡B座2602室</td>
                                                        </tr>
                                                        <tr>
                                                            <th style="background-color: #F3F3F3;">电话:</th>
                                                            <td >0310-2118598</td>
                                                            <th style="background-color: #F3F3F3;">电话:</th>
                                                            <td >18931037275</td>
                                                        </tr>
                                                        <tr>
                                                            <th style="background-color: #F3F3F3;">电子邮箱:</th>
                                                            <td >/</td>
                                                            <th style="background-color: #F3F3F3;">电子邮箱:</th>
                                                            <td >/</td>
                                                        </tr>
                                                    </tbody></table>
                                                    </td>
                                                </tr>
                                                </table>
                             <div class="ycym">
                                <a href="javascript:window.opener=null;window.open('','_self');window.close();">【关闭】</a><a href="javascript:void(0)"  onclick="bt(document.getElementById('article'));" >【打印】</a></div>
                        </div>
                    <br>
                </div>
</div>
	
    </body>
<script>
$(function(){
	 editTable();
	 if(false){
	  $('body').css("background","none")
      $('.infro_table table').css("width","100%")
	  $('.infro_table th').css("text-align","left")
	 }
})
function Bmjypt(infoid){
	var data = {infoid:infoid};
	$.post("Bmjypt",data,function(data){
		if(data.result){
			window.location.href = data.msg;
		}else{
			jsmsg(data.msg);
		}
	})
}
$("#bt").click(function(){
      $(".ycym").css("display","none");  
      
		window.print(); 
		 $(".ycym").css("display",""); 
		});
$(function(){
	var edit_l=$(".editcon p").css("text-indent");
	var edit_left=parseFloat(edit_l);
	if(edit_left<0){
	$(".editcon p").css("text-indent","0");
	};
	var edit_l1=$(".editcon div").css("text-indent");
	var edit_left1=parseFloat(edit_l1);
	if(edit_left1<0){
	$(".editcon div").css("text-indent","0");
	};
	});
</script>
    </html>

'''
soup1 = bs4.BeautifulSoup(html, 'html.parser')
trs = soup1.find_all('#article_con > div > table >  tr')
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