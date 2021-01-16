import os
import xlrd
import threading #多线程处理模块

def pr():
    print('''
 _   _                       
| | | |                     
| |_| | ___ _ __ _ __ _   _ 
|  _  |/ _ \ '__| '__| | | |
| | | |  __/ |  | |  | |_| |
\_| |_/\___|_|  |_|   \__, |
                       __/ |
                      |___/ 
    ''')

def get_url(file): #获取xls or txt文件里不重复的url
    urls = []
    if "xls" in file:
        urls = []
        xls = xlrd.open_workbook(file)
        sheet = xls.sheet_by_name("Sheet1")
        for row in range(1,sheet.nrows):
            url = sheet.cell_value(row,0)
            if "http" in url:
                urls.append(url)
            else:
                urls.append("http://"+url)
        urls = list(set(urls))

    if "txt" in file:
        with open(file,"r") as f:
            for url in f:
                url = url.strip()
                if "http" in url:
                    urls.append(url)
                else:
                    urls.append("http://" + url)
        urls = list(set(urls))

    return urls


def Scan(url,num,se): #执行cmd命令启动xray扫描
    se.acquire()
    os.system("xray.exe webscan --basic-crawler {} --html-output {}.html".format(url,num))
    se.release()

def main():
    for i in range(len(urls)):
        add_thread = threading.Thread(target=Scan,args=(urls[i],i,semaphore)) #调用多线程处理任务
        add_thread.start()

if __name__ == '__main__':
    pr()
    file = input("请输入你要漏扫的xls(爬虫生成后的)或txt文件:")
    num = int(input("请输入进行漏扫所需的线程数:"))
    semaphore = threading.BoundedSemaphore(num) #允许线程同时进行的数量
    urls = get_url(file)
    main()











