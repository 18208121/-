from bs4 import BeautifulSoup
import urllib.request
import re
import csv
from selenium import webdriver
import sys
import time

def getHtml(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(2)
    html = driver.page_source
   # s = quote(url, safe=string.printable)
    #page = urllib.request.urlopen(s)
    #html = page.read()
    return html


def printmoney(ulist):
    tplt = "{:^10}\t{:^50}\t{:^10}\t{:^60}\t{:^40}"
    print(tplt.format("序号","商品名称", "价格", "图片连接","价格连接"))  # 表示格式化输出
    count = 0;
    for i in range(len(ulist)):
        u = ulist[i]
        count = count + 1
        print(tplt.format(count,u[0], u[1], u[2],u[3]))

def urlname(name):
    url = ['https://search.jd.com/Search?keyword='+name+'&wq='+name+'page={}&s=1&click=0'.format(
    i) for i in range(1, 2, 2)]
    return url


def Getdata(html,f,ulist):
    #reg = r'(.+?\.jpg)'
    #imgre = re.compile(reg)
    Regrx = re.compile('\\s|\\￥||\\,|\\[||\\]|\\n|</?[^><]+>')
    Regx = re.compile('[1-9]\\d*\\.\\d*')
    regrx = re.compile('\\[||\\]|')
    soup = BeautifulSoup(html, "html.parser")
    ans = soup.find_all('div', class_='gl-i-wrap')
    z = 0
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
        ulist.append((tds,td,td_1,td_2))
def getImg(html):
    reg = r'src="(.+?\.jpg)" data-lazy-img'    #正则表达式，得到图片地址
    imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
#    html = html.decode('utf-8')
    imglist = re.findall(imgre,html)      #re.findall() 方法读取html 中包含 imgre（正则表达式）的数据
    #把筛选的图片地址通过for循环遍历并保存到本地
    #核心是urllib.request.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve('https:'+imgurl, 'D:\照片\%s.jpg' % x)
        x += 1
    return imglist

def get(a):
    uinfo = []
    f = open('E:/python数据/商品/'+a + '.csv', 'w', encoding='utf-8-sig')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["标题", "价格", "图片链接", "商品链接"])
    urls = urlname(a)
    for url in urls:
        html = getHtml(url)
        Getdata(html, csv_writer, uinfo)
        getImg(html)
    if uinfo:  # 存在值即为真
        return 1
    else:  # list_temp是空的
        return 2

if __name__ == "__main__":
    a = []
    for i in range(1, len(sys.argv)):
        a.append(sys.argv[i])
    print(get(a[0]))