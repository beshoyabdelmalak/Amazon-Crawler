import scrapy
import re


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.com/s?k=laptop&i=computers',
        'https://www.amazon.com/s?k=laptop&i=computers&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cn%3A13896609011&dc&qid=1559821064&rnid=493964&ref=sr_nr_n_2',
        'https://www.amazon.com/s?k=laptop&i=computers&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cn%3A13896615011&dc&qid=1559821064&rnid=493964&ref=sr_nr_n_1'
    ]
    # start_urls = ['https://www.amazon.com/s?k=laptop&i=computers&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cn%3A13896615011&dc&qid=1559821064&rnid=493964&ref=sr_nr_n_1%29']
    # i = 1

    def parse(self, response):
        # get all the urls of the page by following the title of the product
        urls = response.css('.a-color-base .a-text-normal::attr(href)').extract()

        # sometimes it doesn't find any urls so we try one more time
        if len(urls) == 0:
            # print(response.url)
            yield scrapy.Request(url=response.url, callback=self.parse, dont_filter=True)

        # self.log(urls)

        # for every url, crawl the details page
        for url in urls:
            link = response.urljoin(url)
            yield scrapy.Request(url = link, callback= self.parse_details)

        # link = 'https://www.amazon.com/HP-EliteBook-8460p-WINDOWS-Professional/dp/B016PAJAFY'
        # yield scrapy.Request(url=link, callback=self.parse_details)

        # get the next page button, and extract the link inside it
        next_page = response.css('.a-last a::attr(href)').get()
        # if it's not the last page, scrape its next page
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url =next_page, callback=self.parse)


    # scrape the details page
    def parse_details(self, response):
        # get the asin
        asin = response.css('#productDetails_detailBullets_sections1 tr:nth-child(1) td::text').get()

        # fallback
        if asin is None :
            return None

        # another fallback
        if ' ' in asin.strip():
            return None

        # trim all white spaces
        asin = asin.strip()

        # remove all the unwanted data from the url to make it more readable
        link = re.match('https:\/\/www\.amazon\.com\/.*\/dp\/.*\/', response.url.strip())
        # fallback
        if link is None:
            link = re.match('https:\/\/www\.amazon\.com\/dp\/.*\/', response.url.strip())

        link = link.group(0)

        try:
            # write the url of the product in txt file
            f = open('laptops.txt', 'a')
            f.write(link[:-1] +'\n')
            f.close()
        except Exception as e:
            print(format(e))
        # write the content of the details page in xml file
        yield self.writeXML(response, asin)


    def writeXML(sel, response, asin):
        content = response.body.decode('utf-8')
        try:
            f = open('product_xml_files/' + str(asin) + '.xml', 'w')
            f.write(content)
            f.close()
        except Exception as e:
            print(format(e))
