import scrapy

class MingyanSpider(scrapy.Spider):
    name = "mingyan2"
    # def start_requests(self):
    #     urls = [
    #         'http://lab.scrapyd.cn/page/1/',
    #         'http://lab.scrapyd.cn/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)




    start_urls = [  #另外一种写法，无需定义start_requests方法
    'http://www.beiwo.tv/vod/34593/'
    ]




    def parse(self, response):
        
        page =response.url.split("/")[-2]
        
        filename='mingyan5-%s.html' % page
        
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('保存文件：%s' % filename)