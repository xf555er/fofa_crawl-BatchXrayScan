from selenium import webdriver
from selenium.webdriver.common.by import By #获取指定属性元素
from selenium.webdriver.support.ui import WebDriverWait #设置显性等待
from selenium.webdriver.support import expected_conditions as EC #获取元素
from selenium.webdriver.common.keys import Keys  #模拟输入键盘值
from selenium.common.exceptions import TimeoutException #元素操作超时报错
import time #设置时间延迟
import pandas as pd #xls表格处理模块
from pyquery import PyQuery as pq #html处理模块
import random #设置随机数模块

keyword = input("请输入关键词:")
cookie = input("请输入cookie:")
file = input("请输入保存的文件名:")
browser = webdriver.Chrome() #浏览器初始化
cookies = {"name": "_fofapro_ars_session", "path": "/", "secure": False, "value": cookie} #填写你fofa会员账号cookie
lists = []
urls_list = [] #存放资产的url
ips_list = [] #存放资产的ip
countrys_list = [] #存放资产的国家
titles_list = [] #存放资产的标题


def init(): # 获取第一页的数据
    browser.get("https://fofa.so/") #打开fofa网页
    time.sleep(3) #设置时间延迟3秒
    browser.add_cookie(cookies) #添加新的cookie
    time.sleep(2)
    browser.refresh() #网页刷新
    wait = WebDriverWait(browser,10)
    input = wait.until(EC.presence_of_element_located((By.NAME,"q"))) #获取输入框元素
    input.send_keys(keyword) #往输入框输入关键词
    input.send_keys(Keys.ENTER) #输入回车键
    tu = get_data()
    print("资产收集数量:",tu[0],"页数:",tu[1])



def get_data(): #获取资产数据
    html = browser.page_source #获取模拟浏览器当前网页的html
    doc = pq(html)
    numbers = int(doc("#rs > span:nth-child(1)").text().replace(",","")) #资产的数量
    pages = (numbers // 10) + 1 #页数
    urls = doc("#ajax_content > div:nth-child(n) > div.fl.box-sizing > div.re-domain > a").items()
    ips = ip = doc("#ajax_content > div > div.fl.box-sizing > div:nth-child(3) > a").items()
    countrys = doc("#ajax_content > div > div.fl.box-sizing > div:nth-child(4) > a").items()
    titles = doc("#ajax_content > div > div.fl.box-sizing > div:nth-child(2)").items()
    for url in urls:
        if url.text() != "":
            urls_list.append(url.text())
    for ip in ips:
        ips_list.append(ip.text())
    for country in countrys:
        countrys_list.append(country.text())
    for title in titles:
        titles_list.append(title.text())
    for u,i,c,t in zip(urls_list,ips_list,countrys_list,titles_list):
        list = [u,i,c,t]
        lists.append(list)
    return numbers,pages

def next_page():#点击下一页
    try:
        wait = WebDriverWait(browser,10)
        button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#will_page > a.next_page"))) #获取按钮元素
        button.click() #按钮点击
        time.sleep(random.randint(6,8)) #按钮点击的间隔，弄个随机数好应付反爬
        get_data()
    except TimeoutException as e: #
        print("正尝试重新点击下一页....")
        next_page()

def save_xls(lists): #保存到xls表格
    columns = ["urls", "Ips","Countrys","Titles"]
    dt = pd.DataFrame(lists, columns=columns)
    dt.to_excel("{}.xls".format(file), index=0)



def main():
    init()
    time.sleep(4)
    page = int(input("请输入你要爬取的页数:"))
    for i in range(page-1):
        next_page()
    print(lists)
    save_xls(lists)

if __name__ == '__main__':
    main()
