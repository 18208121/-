import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import sys
import time

def getHtml(url):
    options = webdriver.ChromeOptions()
    # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
    options.add_argument('headless')
    # 创建chrome无界面对象
    driver = webdriver.Chrome(chrome_options=options)
    # driver = webdriver.Chrome()
    driver.get(url)
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(2)
    html = driver.page_source
   # s = quote(url, safe=string.printable)
    #page = urllib.request.urlopen(s)
    #html = page.read()
    return html

def otherHtml(url):
    hd = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'}
    try:
        r = requests.get(url, headers=hd, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding  # 把获取到的页面信息 替换成utf-8信息，这样就不会乱码
        print(r.status_code)
        html = r.text
        print(r.url)
        # print(r.text)
    except:
        print("抓取异常")
    return html

def tbhtml(url):
    try:
        header = {
            'authority': 's.taobao.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'referer': 'https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'cna=v1iCFj5e5HUCAWp5DX0quDsv; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; tracknick=shaon1992; tg=0; miid=1632897152788742981; UM_distinctid=16f88fb7505647-021c8a4768c455-c383f64-1fa400-16f88fb7506a97; lgc=shaon1992; enc=bTD3YQaxUUPgMwDFOzNQb7gq%2FH5pgW5AsroLZZNZWAol%2F%2Bq%2FnesRJw6MtTZsB9Nr694mCB7jvjlmb3PQSo3OVA%3D%3D; mt=ci=23_1; t=f85195559e028f48ad19815224752b39; _m_h5_tk=f61d8dd502cb28f5d6db372130b5d45e_1584960506160; _m_h5_tk_enc=a36c7546e631f9f340b6dc44c895175f; tfstk=cC6GBWq-X1R_yzhqNf91DL3u9YeRZEM2rtWCLORQY8cl6tBFilcEa5iTxFbGHj1..; uc3=id2=UUGq1RsrN4lVRg%3D%3D&vt3=F8dBxd9gD5LRH%2BhN35Q%3D&nk2=EFY19v%2BIN9jj&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; uc4=id4=0%40U2OdIeIjT8V0ugGcC5lw5EpiSlBQ&nk4=0%40Eo9LPCpw%2BKOBalOW5iTVFcrXPNw%3D; _cc_=UtASsssmfA%3D%3D; sgcookie=EHwF2Jp4HScWqZwBHzOfu; cookie2=157515f6c454549c82338d09b1970007; _tb_token_=76fe5a3ffb3e8; v=0; alitrackid=item.taobao.com; lastalitrackid=www.taobao.com; uc1=cookie14=UoTUP2D5qVEqyw%3D%3D; JSESSIONID=C3FB11DB6A138C4FEBEEB6CF68BA9B04; l=dBMg_kwlqqvYK87zKOCwdykmBh_OLIRfguyeoWKwi_5Q4_L1lU7OoyHxmEp6cjWAMIxH4cjscS2tZeJgJso4ne2e4AadZxDDB; isg=BBQUyTYnNrtGL6HwNFoBuS4w5VKGbThXLBPCq671_x8imbXjxXzw5_dbmZEBYXCv',
        }  # 隐去了cookie信息和referer信息
        r = requests.get(url, headers=header)  # 获得网页文本
        r.raise_for_status()  # 抛出错误
        r.encoding = r.apparent_encoding  # 编码
        return r.text  # 返回文本
    except:
        print("爬取失败")
        return ""  # 如果错误返回空字符串


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


def pddurlname(name):
    url = 'https://youhui.pinduoduo.com/search/landing?keyword=' + name
    return url

def tburlname(name):
    url = ['https://s.taobao.com/search?q=' + name + '$S={}'.format(
        i) for i in range(44, 87, 44)]
    return url

def tmurlname(name):
    url = ['https://list.tmall.com/search_product.htm?q=' + name +
           '&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton&S={}'.format(
        i) for i in range(0, 120, 60)]
    return url
def Getdata(html,ulist):
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
        ulist.append([tds,td,td_1,td_2,"京东商城"])
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

def Gettpdddata(html,ulist):
    plt = re.findall(r'<span>￥<!-- -->.*?\.\d\d</span></p>', html)  # 获取商品价格
    tlt = re.findall(r'\"goodsName\":\".*?\"', html)  # 商品名
    jlt = re.findall(r'ImageUrl":"https://.+?.jpeg', html)  # 商品图片地址
    wlt = re.findall(r'goodsId=[1-9]\d*', html)  # 商品链接
    for i in range(len(plt)):
        price = plt[i].split('-->')[1].split('</span>')[0]
        title = tlt[i].split(':"')[1].split('"')[0]
        img = jlt[i].split(':"')[1]
        spid = wlt[i].split('=')[1]
        sp = 'https://youhui.pinduoduo.com/goods/goods-detail?goodsId=' + spid
        ulist.append([title, price, img, sp, "拼多多"])

def Gettbdata(html,ulist):
    try:
        plt = re.findall(r'\"view_price\":\"\d+\.\d*\"', html)  # 正则匹配，返回值是列表形式
        tlt = re.findall(r'\"raw_title\":\".*?\"', html)
        jlt = re.findall(r'(?<=pic_url":").*?","detail_url', html)  # 商品图片地址
        wlt = re.findall(r'"nid":"[1-9]\d*', html)  # 商品链接
        # print(tlt)
        print(len(plt))
        for i in range(len(plt)):  # 遍历所有的列表中的项
            price = eval(plt[i].split('\"')[3])  # 去掉双引号，以：分割字符串
            title = tlt[i].split('\"')[3]
            photo = jlt[i].split('","')[0]
            photo = 'https:' + photo
            spid = wlt[i].split(':"')[1]
            sp = 'https://item.taobao.com/item.htm?ft=t&spm=a230r.1.14.42.4a606a14Kz27Qe&id=' + spid + '&ns=1&abbucket=2'
            ulist.append([title, price, photo, sp, "淘宝"])  # 把商品信息添加到ilt中
    except:
        print("...")

def Gettmdata(html,ulist):
    try:
        plt = re.findall(r'<b>&yen;</b>.*?\.\d\d', html)  # 获取商品价格
        tlt = re.findall(r'target=\"_blank\" title=\".*?\"', html)  # 商品名
        jlt = re.findall(r'data-ks-lazyload=  "//.+?.jpg', html)  # 商品图片地址
        wlt = re.findall(r'<a href="//.+?" target="_blank" title="', html)  # 商品链接
        for i in range(len(plt)):
            price = plt[i].split('/b>')[1]
            title = tlt[i].split('e="')[1].split('"')[0]
            img = jlt[i].split('"')[1]
            spid = wlt[i].split('f="')[1].split('" ta')[0]
            ulist.append([price, title, img, spid,"天猫"])
    except:
        print(" ")

def get(a):
    uinfo = []
    f = open('E:/python数据/商品/'+a + '.txt', 'w', encoding='utf-8')
    urls = urlname(a)
    for url in urls:
        html = getHtml(url)
        Getdata(html, uinfo)
      #  getImg(html)
    pdd_url = pddurlname(a)
    pdd_html = otherHtml(pdd_url)
    Gettpdddata(pdd_html,uinfo)
    tb_url = tburlname(a)
    for tburl in tb_url:
        tb_html = tbhtml(tburl)
        Gettbdata(tb_html, uinfo)
    tm_url = tmurlname(a)
    for tmurl in tm_url:
        tm_html = tbhtml(tmurl)
        Gettmdata(tm_html, uinfo)
    for i in uinfo:  # 对于双层列表中的数据
        i = str(i).strip('[').strip(']').replace('\'', '') + '\n'  # 将其中每一个列表规范化成字符串
        f.write(i)
    if uinfo:  # 存在值即为真
        return 1
    else:  # list_temp是空的
        return 2

if __name__ == "__main__":
    a = []
    for i in range(1, len(sys.argv)):
        a.append(sys.argv[i])
    print(get(a[0]))