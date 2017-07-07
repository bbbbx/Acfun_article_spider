# -*- coding: utf-8 -*-
import scrapy
import urlparse
from scrapy.http import Request
from Acfun_article_spider.items import AcfunArticleSpiderItem

class AcfunArticleSpider(scrapy.Spider):
    name = "Acfun_article"
    allowed_domains = ["http://www.acfun.cn/v/list73/index.htm"]
    start_urls = ['http://www.acfun.cn/v/list73/index.htm']

    def parse(self, response):
        article_nodes = response.css('#block-content-article .mainer .item a.title')

        for article_node in article_nodes:
            article_url = urlparse.urljoin(response.url, str(article_node.css("::attr(href)").extract_first(
                "")))  # "http://www.acfun.cn" + str(article_node.css("::attr(href)").extract_first(""))
            yield Request(url=article_url, callback=self.parse_detail, dont_filter=True)

        next_nodes = response.css(".pager")
        next_node = next_nodes[len(next_nodes) - 1]
        next_url = str(next_node.css("::attr(href)").extract_first(""))
        if next_url:
            next_url = urlparse.urljoin(response.url, next_url)
            yield Request(url=next_url, callback=self.parse, dont_filter=True)

    def parse_detail(self, response):
        title = response.css(".txt-title-view_1::text").extract_first("")  # 文章标题
        create_date = response.css("#block-data-view::attr(data-date)").extract_first("")  # 创建日期
        url = response.url
        author = response.css("nobr::text").extract_first("")  # 文章UP主
        content = response.css("#area-player").extract_first("")  # 文章内容
        tags = response.css("#block-data-view::attr(data-tags)").extract_first("")  # 文章标签
        comment_nums = response.css("#block-data-view::attr(data-comms)").extract_first("")  # 评论数
        view_nums = response.css("#block-data-view::attr(data-views)").extract_first("")  # 围观数
        fav_nums = response.css("#block-data-view::attr(data-favors)").extract_first("")  # 收藏数

        ac_article_item = AcfunArticleSpiderItem()
        ac_article_item["title"] = title
        ac_article_item["create_date"] = create_date
        ac_article_item["url"] = url
        ac_article_item["author"] = author
        ac_article_item["content"] = content
        ac_article_item["tags"] = tags
        ac_article_item["comment_nums"] = comment_nums
        ac_article_item["view_nums"] = view_nums
        ac_article_item["fav_nums"] = fav_nums

        yield ac_article_item
