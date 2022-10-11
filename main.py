import requests
import parsel
import re

def element(url, sele, ref):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"}
    # 请求
    response3 = requests.get(url, headers=header)
    # 解码
    response3.encoding = 'utf-8'
    selector3 = parsel.Selector(response3.text)
    funds = selector3.css(sele).get()
    # 正则表达式
    q1 = re.findall(ref, funds)
    # q2 = re.findall(ref2, funds)
    # q3 = re.findall(ref3, funds)
    q1 = "".join(q1)
    return q1


def fund(url_funds):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"}
    # 请求
    response3 = requests.get(url_funds, headers=header)
    # 解码
    response3.encoding = 'utf-8'
    selector3 = parsel.Selector(response3.text)
    funds = selector3.css('div.priceInfo-DS-EntryPoint1-1 > div').get()
    # 正则表达式
    q1 = re.findall(
        '<div class="mainPrice color_green-DS-EntryPoint1-1">(.*?)</div>', funds)
    q2 = re.findall('<!-- -->(.*?)<!-- -->', funds)
    # # 列表转字符串
    funds = "".join(q1)
    trend = ",".join(q2)
    result = "价格：" + funds + "     " + "幅度: " + trend
    return result


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"}

url_wea = "https://www.tianqi.com/yuhuaqu/"
url_con = "https://m.xzw.com/fortune/cancer/0/"
url_funds1 = "https://www.msn.cn/zh-cn/money/watchlist?ocid=msedgntp&duration=1D&id=adfh77"
url_funds2 = "https://www.msn.cn/zh-cn/money/watchlist?ocid=msedgntp&duration=1D&id=ah7etc"
url_funds3 = "https://www.msn.cn/zh-cn/money/watchlist?ocid=msedgntp&duration=1D&id=a6qja2"


# 天气信息获取
# 请求天气网站
response = requests.get(url_wea, headers=header)
# 解码
response.encoding = 'utf-8'
selector = parsel.Selector(response.text)
# 定位
weather = selector.css(
    "body > div.weatherbox > div > div.left > dl > dd.weather > span").get()
wind = selector.css(
    'body > div.weatherbox > div > div.left > dl > dd.shidu > b:nth-child(2)').get()
date = selector.css(
    'body > div.weatherbox > div > div.left > dl > dd.week').get()
# 正则表达式
a = re.findall('<span><b>(.*?)</b>', weather)
b = re.findall('</b>(.*?)</span>', weather)
c = re.findall('<b>风向：(.*?)</b>', wind)
d = re.findall('<dd class="week">(.*?)</dd>', date)
# list to string
state = ''.join(a)
temp = ''.join(b)
wind = ''.join(c)
date = ''.join(d)
print(a, b, c, d)
print(state, temp, wind, date)


# # 星座运势
sele2 = 'li.p1 > div > p'
ref = '<p>(.*?)<small>'
positioning = element(url_con, sele2, ref)

# 基金
funds1 = fund(url_funds1)
funds2 = fund(url_funds2)
funds3 = fund(url_funds3)

# 邮件发送
# host_server = 'smtp.163.com'  # qq邮箱smtp服务器
# sender_qq = '17692230708@163.com'  # 发件人邮箱
# pwd = 'BIHNWZMSKURYQDAI'
# receiver = ["771457766@qq.com"]  # 收件人邮箱
# mail_title = '天气邮件'  # 邮件标题


file = open("mydata.html", 'w+', encoding='UTF-8')
file.write("####日常信息####" + "\n"\
    "日期----" + date + "\n"\
    "裕华今日----" + state + "\n"\
    "温度范围----" + temp + "\n"\
    "风向----" + wind + "\n"\
    "巨蟹座今日运势----" + positioning + "\n"\
    "\n"\
    "####基金####" + "\n"\
    "上证指数:" + funds1 + "\n"\
    "恒生指数:" + funds2 + "\n"\
    "道琼斯指数:" + funds3)
file.close()