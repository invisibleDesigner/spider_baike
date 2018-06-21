# -*- coding: utf-8 -*-

__author__ = 'YangChang'

from crawler.spider_baike import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
    def __init__(self):
        # url 管理器
        self.urls = url_manager.UrlManager()
        # 网页下载器
        self.downloader = html_downloader.HtmlDownloader()
        # 网页解析器
        self.parser = html_parser.HtmlParser()
        # 数据输出器
        self.outputer = html_outputer.HtmlOutputer()
    def craw(self, root_url):
        # count 访问url计数
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                # 获取新url
                new_url = self.urls.get_new_url()
                print('正在爬取craw %d : %s' % (count, new_url))
                # 下载对应url下的内容
                html_cont = self.downloader.download(new_url)
                # 解析网页，获得新的链接和网页内容
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 把新的链接加入代码池
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                #用count控制爬取链接的次数
                if count == 100:
                    break
                count = count + 1
            except:
                print('crawl fail!')
        self.outputer.output_html()

if __name__ == "__main__":
    print('=====爬虫开始=====')
    root_url = "https://baike.baidu.com/item/李庚/20162559"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    print('=====爬虫结束=====')