from imp import reload
import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import sys
import time
from multiprocessing.dummy import Pool as ThreadPool
from functools import partial


def getHtml(url):
    # options = webdriver.ChromeOptions()
    # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
    # options.add_argument('headless')
    # 创建chrome无界面对象
    # driver = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Chrome()
    driver.get(url)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(2)
    html = driver.page_source
    # s = quote(url, safe=string.printable)
    # page = urllib.request.urlopen(s)
    # html = page.read()
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


def urlname(name):
    url = ['https://search.jd.com/Search?keyword=' + name + '&wq=' + name + 'page={}&s=1&click=0'.format(
        i) for i in range(1, 8, 2)]
    return url


def pddurlname(name):
    url = 'https://youhui.pinduoduo.com/search/landing?keyword=' + name
    return url


def tburlname(name):
    url = ['https://s.taobao.com/search?q=' + name + '$S={}'.format(
        i) for i in range(44, 89, 44)]
    return url


def tmurlname(name):
    url = ['https://list.tmall.com/search_product.htm?q=' + name +
           '&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton&S={}'.format(
               i) for i in range(0, 121, 60)]
    return url


def Getdata(url, ulist):
    # driver = webdriver.Chrome()
    # driver.get(url)
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    # time.sleep(2)
    # html = driver.page_source
    head = {'authority': 'search.jd.com',
            'method': 'GET',
            'path': '/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=4&s=84&scrolling=y&log_id=1529828108.22071&tpl=3_M&show_items=7651927,7367120,7056868,7419252,6001239,5934182,4554969,3893501,7421462,6577495,26480543553,7345757,4483120,6176077,6932795,7336429,5963066,5283387,25722468892,7425622,4768461',
            'scheme': 'https',
            'referer': 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=3&s=58&click=0',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'Cookie': 'qrsc=3; pinId=RAGa4xMoVrs; xtest=1210.cf6b6759; ipLocation=%u5E7F%u4E1C; _jrda=5; TrackID=1aUdbc9HHS2MdEzabuYEyED1iDJaLWwBAfGBfyIHJZCLWKfWaB_KHKIMX9Vj9_2wUakxuSLAO9AFtB2U0SsAD-mXIh5rIfuDiSHSNhZcsJvg; shshshfpa=17943c91-d534-104f-a035-6e1719740bb6-1525571955; shshshfpb=2f200f7c5265e4af999b95b20d90e6618559f7251020a80ea1aee61500; cn=0; 3AB9D23F7A4B3C9B=QFOFIDQSIC7TZDQ7U4RPNYNFQN7S26SFCQQGTC3YU5UZQJZUBNPEXMX7O3R7SIRBTTJ72AXC4S3IJ46ESBLTNHD37U; ipLoc-djd=19-1607-3638-3638.608841570; __jdu=930036140; user-key=31a7628c-a9b2-44b0-8147-f10a9e597d6f; areaId=19; __jdv=122270672|direct|-|none|-|1529893590075; PCSYCityID=25; mt_xid=V2_52007VwsQU1xaVVoaSClUA2YLEAdbWk5YSk9MQAA0BBZOVQ0ADwNLGlUAZwQXVQpaAlkvShhcDHsCFU5eXENaGkIZWg5nAyJQbVhiWR9BGlUNZwoWYl1dVF0%3D; __jdc=122270672; shshshfp=72ec41b59960ea9a26956307465948f6; rkv=V0700; __jda=122270672.930036140.-.1529979524.1529984840.85; __jdb=122270672.1.930036140|85.1529984840; shshshsID=f797fbad20f4e576e9c30d1c381ecbb1_1_1529984840145'
            }
    r = requests.get(url, headers=head)  # 获得网页文本
    r.raise_for_status()  # 抛出错误
    r.encoding = r.apparent_encoding  # 编码
    html = r.text
    # reg = r'(.+?\.jpg)'
    # imgre = re.compile(reg)
    Regrx = re.compile('\\s|\\￥||\\,|\\[||\\]|\\n|</?[^><]+>')  # 匹配标签与空格
    Regx = re.compile('[1-9]\\d*\\.\\d*')  # 匹配价格信息
    regrx = re.compile('\\[||\\]|')  # 匹配空格
    soup = BeautifulSoup(html, "html.parser")
    ans = soup.find_all('div', class_='gl-i-wrap')
    z = 0
    for data in ans:
        tds = data('em')
        if (str(tds).isspace() == False):
            tds = Regrx.sub('', str(tds))
        tds_1 = data.i
        td = Regx.findall(str(tds_1))
        td = regrx.sub('', str(td))
        td = td.replace("'", "")
        tds_2 = data.img
        td_1 = tds_2['src']
        tds_3 = data.a
        td_2 = tds_3['href']
        ulist.append([tds, td, td_1, td_2, "京东商城"])


def getImg(html):
    reg = r'src="(.+?\.jpg)" data-lazy-img'  # 正则表达式，得到图片地址
    imgre = re.compile(reg)  # re.compile() 可以把正则表达式编译成一个正则表达式对象.
    #    html = html.decode('utf-8')
    imglist = re.findall(imgre, html)  # re.findall() 方法读取html 中包含 imgre（正则表达式）的数据
    # 把筛选的图片地址通过for循环遍历并保存到本地
    # 核心是urllib.request.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve('https:' + imgurl, 'D:\照片\%s.jpg' % x)
        x += 1
    return imglist


def Gettpdddata(url, ulist):
    hd = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'}
    for i in range(1, 3):
        formdata = {'type': 'index',
                    'paged': i}  # 对每一个页面进行处理，使用for循环
        try:
            try:
                r = requests.get(url, data=formdata, timeout=30)
                r.raise_for_status()
                r.encoding = r.apparent_encoding  # 把获取到的页面信息 替换成utf-8信息，这样就不会乱码
                html = r.text
            except:
                print("抓取异常")
            try:
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
            except:
                print(" ")
        except:
            continue  # 如果某一个页面解析出了entity，那么继续解析下一个页面。
        time.sleep(2)


def Gettbdata(url, ulist):
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
    html = r.text
    try:
        plt = re.findall(r'\"view_price\":\"\d+\.\d*\"', html)  # 正则匹配，返回值是列表形式
        tlt = re.findall(r'\"raw_title\":\".*?\"', html)
        jlt = re.findall(r'(?<=pic_url":").*?","detail_url', html)  # 商品图片地址
        wlt = re.findall(r'"nid":"[1-9]\d*', html)  # 商品链接
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


def Gettmdata(url, ulist):
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
    html = r.text  # 返回文本
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
            ulist.append([price, title, img, spid, "天猫"])
    except:
        print(" ")


if __name__ == "__main__":
    a = []
    for i in range(1, len(sys.argv)):
        a.append(sys.argv[i])
    pool = ThreadPool(8)  # 双核电脑
    tot_page = []
    tot_page_1 = []
    tot_page_3 = []
    uinfo = []
    f = open('E:/python数据/商品/' + a[0] + '.txt', 'w', encoding='utf-8')
    urls = tburlname(a[0])
    for url in urls:
        tot_page.append(url)
    tm_urls = tmurlname(a[0])
    for url in tm_urls:
        tot_page_1.append(url)
    jd_urls = urlname(a[0])
    for url in jd_urls:
        tot_page_3.append(url)
    pool.map(partial(Gettbdata, ulist=uinfo), tot_page)  # 多线程工作
    pool.map(partial(Gettmdata, ulist=uinfo), tot_page_1)
    pool.map(partial(Getdata, ulist=uinfo), tot_page_3)
    pdd_url = pddurlname(a[0])
    Gettpdddata(pdd_url, uinfo)
    for i in uinfo:  # 对于双层列表中的数据
        i = str(i).strip('[').strip(']').replace('\'', '') + '\n'  # 将其中每一个列表规范化成字符串
        f.write(i)
    pool.close()
    pool.join()
    if uinfo:  # 存在值即为真
        print(1)
    else:  # list_temp是空的
        print(1)