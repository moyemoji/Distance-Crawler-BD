# DistanceCrawler
基于百度Javascript API的驾车路线规划方案时间、距离Python小爬虫。

## 概述
使用百度地图API获取两点之间通行距离和时间有两种方式，一种是构造url直接访问接口，另一种是编写前端界面用JS调用。前者的好处是速度快，但对访问量及并发都有限制，后者慢一些，但是没有访问量上的限制，如果增加线程数也能实现数据快速的获取。

DistanceCrawler基于百度Javascript API及Selenium，将爬取通行时间和距离的功能二次封装成Python接口。使用的时候只需传入起始点和终点相关信息，即可得到结果。

## 环境配置
```
yum -y install python3

pip install selenium

# 另外需要下载chromedriver.exe，将其保存地址添加至环境变量
```

## 使用说明
1. import距离爬虫DistanceCrawler
2. 实例化一个DistanceCrawler
3. 调用实例对象getDistance方法
4. 调用实例对象stopBrowser方法关闭浏览器释放资源

## 使用示例
```
from DistanceCrawler import *

if  __name__ == '__main__':
    distance_crawler = DistanceCrawler()
    dataset = ['{"startid":1, "endid":2, "lonstart":113.41, "latstart":29.58, "lonend":113.40, "latend":29.50}',
               '{"startid":1, "endid":2, "lonstart":113.41, "latstart":29.58, "lonend":113.40, "latend":29.51}',
               '{"startid":1, "endid":2, "lonstart":113.41, "latstart":29.58, "lonend":113.40, "latend":29.52}']
               
    for data in dataset:
        result = distance_crawler.getDistance(data)
        print(result)
```
