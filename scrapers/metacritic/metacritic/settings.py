# Scrapy settings for metacritic project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'metacritic'

SPIDER_MODULES = ['metacritic.spiders']
NEWSPIDER_MODULE = 'metacritic.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'metacritic (+http://www.yourdomain.com)'
