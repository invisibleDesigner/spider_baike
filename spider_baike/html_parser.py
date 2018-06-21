# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.parse
import re

class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        # soup = BeautifulSoup(html_cont, 'html.parser', from_encoding = 'utf-8') from_encoding pyhotn 默认unicode编码
        # from_encoding会被忽视
        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href = re.compile(r'/item'))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_date = {}

        # url
        res_date['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_ = "lemmaWgt-lemmaTitle-title").find("h1")
        res_date['title'] = title_node.get_text()

        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node =  soup.find('div', class_ = "lemma-summary")
        res_date['summary'] = summary_node.get_text()

        return res_date