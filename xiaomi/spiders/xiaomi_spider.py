import scrapy
import re
from scrapy.selector import Selector
from xiaomi.items import XiaomiItem

class XiaomiSpider(scrapy.Spider):
    name="xiaomi"
    allowed_domains=["mi.com"]
    start_urls=[]
    base = "http://app.mi.com/category/"
    i=1
    while i<30:
    	if i==15:
    	    i=i+1
    	    continue	
        url=base+str(i)+"#page=0"
        start_urls.append(url)
        i=i+1

    # def find_next_page(self,url):
    #     try:
    #         page_num_str=url.split('=')[-1]
    #         page_num = int(page_num_str)+1
    #         url=url[:-len(page_num_str)]+str(page_num)
    #         print "url modified by Yan ",url
    #         return url
    #     except ValueError:
    #         print "### page cannot be handled: ",
    #         print url
    #         return "http://google.com"

    def parse(self,response):
        apps=Selector(response).xpath('//ul[@id="all-applist"]/li')
        for app in apps:
            item=XiaomiItem()
            name=app.xpath('.//h5/a/text()').extract_first().encode('utf-8')
            item['name']=app.xpath('.//h5/a/text()').extract_first().encode('utf-8')
            item['url']=app.xpath('.//h5/a/@href').extract()
            item['category']=app.xpath('.//p/a/text()').extract_first().encode('utf-8')
            #print item['category']," ",item['name'],,,,
            yield item
