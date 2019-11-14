import scrapy
import re
import os


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AAcer&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_0',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AAlienware&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_1',
        'https://www.amazon.com/s/ref=sr_in_-2_p_89_2?fst=as%3Aoff&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Ck%3Alaptop%2Cp_89%3AApple&bbn=565108&keywords=laptop&ie=UTF8&qid=1560104316&rnid=2528832011',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AASUS&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_3',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AAVENTIS+SYSTEMS&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_4',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AComputer+Upgrade+King&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_5',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3ACTL&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_6',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3ADell&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_7',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AEluktronics&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_9',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AEXcaliberPC&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_10',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AFujitsu&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_11',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AGateway&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_12',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AGeneric&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_13',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AGigabyte&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_14',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AHEWLETT+PACKARD&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_15',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AHIDevolution&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_18',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AHP&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_19',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AHUAWEI&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_20',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AIBM&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_22',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AJumper&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_23',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3ALatitude&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_25',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3ALenove&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_26',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3ALenovo&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_27',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3ALenovo+Group+Limited&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_28',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3ALG&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_29',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AME2+MichaelElectronics2&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_30',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AMerkAmerica&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_31',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AMicrosoft&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_32',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AMSI&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_33',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3APanasonic&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_34',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3APROSTAR&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_35',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AQuality+Refurbished+Computers&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_37',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3ARazer&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_38',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3ARCA&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_39',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3ASager&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_41',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3ASamsung&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_42',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3ASony&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_44',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AToshiba&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_46',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AToughbook&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_47',
        'https://www.amazon.com/s?k=laptop&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AXOTIC+PC&dc&fst=as%3Aoff&qid=1560104316&rnid=2528832011&ref=sr_in_-2_p_89_50',
    ]
    # start_urls = ['https://www.amazon.com/s?k=laptop&i=electronics&ref=nb_sb_noss_1']

    def parse(self, response):
        # get all the urls of the page by following the title of the product
        urls = response.css('.a-color-base .a-text-normal::attr(href)').extract()

        # sometimes it doesn't find any urls so we try one more time
        if len(urls) == 0:
            yield scrapy.Request(url=response.url, callback=self.parse, dont_filter=True)

        # for every url, crawl the details page
        for url in urls:
            link = response.urljoin(url)
            yield scrapy.Request(url = link, callback= self.parse_details)

        # link = response.urljoin(urls[0])
        # yield scrapy.Request(url=response.url, callback=self.parse_details)

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
        if asin is None:
            return None

        # another fallback
        if ' ' in asin.strip():
            return None

        # trim all white spaces
        asin = asin.strip()

        print("crawling {} file ".format(asin))
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



        reviews = response.css("#reviews-medley-footer .a-text-bold::attr(href)").get()
        if reviews:
          reviews_page = response.urljoin(reviews)
          yield scrapy.Request(url=reviews_page, callback=self.parse_reviews,meta={'asin': asin})


    # scrape the reviews page
    def parse_reviews(self, response):
      # get the asin
      asin = response.meta['asin']

      yield self.writeReviewXML(response, asin)
      next_page = response.css(".a-last a::attr(href)").get()
      if next_page :
        next_page = response.urljoin(next_page)
        yield scrapy.Request(url=next_page, callback=self.parse_reviews,meta={'asin': asin})



    def writeXML(self, response, asin):
        content = response.body.decode('utf-8')
        filename ="product_xml_files/" + asin + ".xml"

        if os.path.exists(filename):
          append_write = 'a'  # append if already exists
        else:
          append_write = 'w'  # make a new file if not

        try:
            f = open(filename, append_write)
            f.write(content)
            f.close()
        except Exception as e:
            print(format(e))

    def writeReviewXML(self, response, asin):
        content = response.body.decode('utf-8')
        filename ="review_xml_files/" + asin + ".xml"
        try:
            f = open(filename, 'a')
            f.write("<div class=asin>" + asin + "</div>")
            f.write(content)
            f.close()
        except Exception as e:
            print(format(e))
