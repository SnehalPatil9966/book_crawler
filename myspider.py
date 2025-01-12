import scrapy
import json
from pymongo import MongoClient


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def _init_(self):
        self.client = MongoClient('127.0.0.1', 27017)
        self.db = self.client['product_db']
        self.collection = self.db['products']
    
    def parse(self, response):
        products = response.xpath('//article[@class="product_pod"]')
        raw_data = []
        cleaned_data = []

        for product in products:
            product_name = product.xpath('.//h3/a/text()').get()
            price = product.xpath('.//p[@class="price_color"]/text()').get()
            rating = product.xpath('.//p[contains(@class, "star-rating")]/@class').get().split()[-1]
            availability = product.xpath('.//p[@class="instock availability"]/text()').getall()
            availability = ''.join(availability).strip()

            # Store raw data
            raw_data.append({
                'product_name': product_name,
                'price': price,
                'rating': rating,
                'availability': availability
            })

            # Clean and process data
            product_name = product_name.strip() if product_name else 'N/A'
            price = price.strip().replace('£', '') if price else '0.00'
            rating = rating.strip() if rating else 'No rating'
            availability = availability.strip() if availability else 'Unknown'

            cleaned_data.append({
                'product_name': product_name,
                'price': float(price),
                'rating': rating,
                'availability': availability
            })

        # Save raw data to a JSON file
        with open('raw_products.json', 'w') as f:
            json.dump(raw_data, f, indent=4)

        # Save cleaned data to a JSON file
        with open('cleaned_products.json', 'w') as f:
            json.dump(cleaned_data, f, indent=4)

        # Insert cleaned data into MongoDB
        self.collection.insert_many(cleaned_data)

        #print("Sample data inserted successfully!")

       # # Print the cleaned data
        #for item in cleaned_data:
         #   self.log(f"Product: {item['product_name']}, Price: {item['price']}, Rating: {item['rating']}, Availability: {item['availability']}")

        # Follow pagination link to the next page
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
           yield response.follow(next_page, self.parse)
