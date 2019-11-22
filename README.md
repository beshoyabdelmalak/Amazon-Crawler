# Amazon-Crawler
crawl all laptops from amazon and save them in xml files in python using Scrapy, scrapy-user-agents, scrapy-rotating-proxies

# Install Packages :

# Scrapy :
install scrapy using the following command :
pip install Scrapy

See the Documentation here : https://doc.scrapy.org/

# scrapy-user-agents:
install the package using the following command:
pip install scrapy-user-agents

See the Documentation here : https://github.com/hyan15/crawler-demo/tree/master/crawling-basic/scrapy_user_agents

# scrapy-rotating-proxies:
install the package using the following command: 
pip install scrapy-rotating-proxies

See the Documentation here : https://github.com/TeamHG-Memex/scrapy-rotating-proxies

# Run the spider:

navigate to Amazon-Crawler/crawler/crawler
then run the command : scrapy crawl amazon

# Result:

after the spider finishes, you can find the xml files insind Amazon-Crawler/crawler/crawler/product-xml-files
and the links of the crawled products in Amazon-Crawler/crawler/crawler/laptops.txt

# Scrape other products:

you will have to paste the link of the department you want to crawl inside start_urls array which is located in 
Amazon-Cralwer/crawler/crawler/spiders/amazon.py
