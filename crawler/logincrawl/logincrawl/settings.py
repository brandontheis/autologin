# -*- coding: utf-8 -*-

# Scrapy settings for logincrawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'logincrawl'

SPIDER_MODULES = ['logincrawl.spiders']
NEWSPIDER_MODULE = 'logincrawl.spiders'

#grab max of 1000 pages on site looking for login
CLOSESPIDER_ITEMCOUNT = '1000'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'logincrawl (+http://www.hyperiongray.com)'