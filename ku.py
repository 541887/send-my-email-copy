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
