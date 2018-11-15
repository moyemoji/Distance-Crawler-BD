from DistanceCrawler import *

if  __name__ == '__main__':
    distance_crawler = DistanceCrawler()
    dataset = ['{"startid":1, "endid":2, "lonstart":113.41, "latstart":29.58, "lonend":113.40, "latend":29.50}',
               '{"startid":1, "endid":2, "lonstart":113.41, "latstart":29.58, "lonend":113.40, "latend":29.51}',
               '{"startid":1, "endid":2, "lonstart":113.41, "latstart":29.58, "lonend":113.40, "latend":29.52}',
               '{"startid":1, "endid":2, "lonstart":113.41, "latstart":29.58, "lonend":113.40, "latend":29.53}',
               '{"startid":1, "endid":2, "lonstart":113.41, "latstart":29.58, "lonend":113.40, "latend":29.54}',
               '{"startid":1, "endid":2, "lonstart":113.41, "latstart":29.58, "lonend":113.40, "latend":29.55}',]
    for data in dataset:
        result = distance_crawler.getDistance(data)
        print(result)

