# -*- coding:utf-8 -*-
__author__ = 'venus'
# 用于调试debug
from scrapy.cmdline import execute
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "Acfun_article"])