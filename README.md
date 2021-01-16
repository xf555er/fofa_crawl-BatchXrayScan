# 一、环境:python3
***
# 二、使用方法
## 下载相对应谷歌浏览器版本的chromedriver（谷歌驱动），然后放到谷歌浏览器的application目录里，并将application目录设置成环境变量

***
## 如果你使用是py文件则需安装爬虫所需的库,使用的是exe就不用了
```pip install -r requirements.txt```
***
## 去fofa登录你的账号，然后获取cookie
![image](https://github.com/xf555er/fofa_crawl/blob/master/images/%E8%8E%B7%E5%8F%96cookie.png)
***
## 进入爬虫文件所在目录,执行爬虫文件，爬取结果会以xls文档保存
```
python fofa.py
```
![image](https://github.com/xf555er/fofa_crawl/blob/master/images/1.png)
***
## 这里我弄了个Xray的批量扫描，扫描的文件可以是爬取后生成的xls文档或者你自己弄的txt文件
```python Xray_Scan.py```
![image](https://github.com/xf555er/fofa_crawl-BatchXrayScan/blob/master/images/xray%E6%89%B9%E9%87%8F%E6%89%AB%E6%8F%8F.png)
