import requests
from bs4 import BeautifulSoup
import urllib.request
import re
from urllib.parse import quote
import string
import csv


def getHtml(url):
    s = quote(url, safe=string.printable)
    page = urllib.request.urlopen(s)
    html = page.read()
    return html


def printmoney(ulist):
    print(ulist)

def urlname(name):
    url = 'https://search.jd.com/Search?keyword='+name+'&wq='+name+'page=1&s=1&click=0'
    return url


def Getdata(html,f):
    #reg = r'(.+?\.jpg)'
    #imgre = re.compile(reg)
    Regrx = re.compile('\\s|\\￥||\\,|\\[||\\]|\\n|</?[^><]+>')
    Regx = re.compile('[1-9]\\d*\\.\\d*')
    regrx = re.compile('\\[||\\]|')
    soup = BeautifulSoup(html, "html.parser")
    ans = soup.find_all('div', class_='gl-i-wrap')
    for data in ans:
        tds = data('em')
        if(str(tds).isspace() == False):
             tds = Regrx.sub('',str(tds))
        tds_1 = data.i
        td = Regx.findall(str(tds_1))
        td = regrx.sub('',str(td))
        td = td.replace("'","")
        tds_2 = data.img
        td_1 = tds_2['src']
        tds_3 = data.a
        td_2 = tds_3['href']
        f.writerow((tds,td,td_1,td_2))

def getImg(html):
    reg = r'src="(.+?\.jpg)" data-lazy-img'    #正则表达式，得到图片地址
    imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
    html = html.decode('utf-8')
    imglist = re.findall(imgre,html)      #re.findall() 方法读取html 中包含 imgre（正则表达式）的数据
    #把筛选的图片地址通过for循环遍历并保存到本地
    #核心是urllib.request.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
    x = 0

    for imgurl in imglist:
        urllib.request.urlretrieve('https:'+imgurl, 'D:\照片\%s.jpg' % x)
        x += 1
    return imglist

def main():
    print("请输入商品")
    a = input()
    f = open(a+'.csv', 'w', encoding='utf-8-sig')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["标题", "价格", "图片链接","商品链接"])
    jdurl = urlname(a)
    html = getHtml(jdurl)
    getImg(html)
    Getdata(html,csv_writer)

main()