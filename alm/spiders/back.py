# import re
# import scrapy
# from scrapy.loader import ItemLoader
# from ..items import AlmItem
# from itemloaders.processors import TakeFirst
# import requests
# import json
#
# pattern = r'(\xa0)?'
# page = 1
# url = f"https://www.almbrand.dk/api/v1/news/search?id=65020&page={page}"
#
# payload = {}
# headers = {
#     'authority': 'www.almbrand.dk',
#     'pragma': 'no-cache',
#     'cache-control': 'no-cache',
#     'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
#     'accept': 'application/json, text/plain, */*',
#     'request-id': '|RdDsZ.C9fwn',
#     'sec-ch-ua-mobile': '?0',
#     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
#     'request-context': 'appId=cid-v1:3993aba1-8e9f-4184-b1a9-2c9b8ef0d6fb',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://www.almbrand.dk/om-alm-brand/presse/nyhed/',
#     'accept-language': 'en-US,en;q=0.9',
#     'cookie': 'ai_user=S0IWJ|2021-03-08T12:23:01.618Z; CookieInformationConsent=%7B%22website_uuid%22%3A%22f2d5e12f-193f-4b9f-beae-1aeef267b152%22%2C%22timestamp%22%3A%222021-03-08T12%3A23%3A03.066Z%22%2C%22consent_url%22%3A%22https%3A%2F%2Fwww.almbrand.dk%2F%3Fint_cmpid%3DPB%253Adefault_presse_1%22%2C%22consent_website%22%3A%22almbrand.dk%22%2C%22consent_domain%22%3A%22www.almbrand.dk%22%2C%22user_uid%22%3A%22b421039c-19fb-452c-aea0-49f6086e1e87%22%2C%22consents_approved%22%3A%5B%22cookie_cat_necessary%22%2C%22cookie_cat_functional%22%2C%22cookie_cat_statistic%22%2C%22cookie_cat_marketing%22%2C%22cookie_cat_unclassified%22%5D%2C%22consents_denied%22%3A%5B%5D%2C%22user_agent%22%3A%22Mozilla%2F5.0%20%28Windows%20NT%206.1%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F88.0.4324.190%20Safari%2F537.36%22%7D; _fbp=fb.1.1615206183391.1880895253; .EPiForm_BID=4aeee55e-4431-4511-afc7-b64a7a45078b; .EPiForm_VisitorIdentifier=4aeee55e-4431-4511-afc7-b64a7a45078b:; EPi:StateMarker=true; EPiSessionId=c2ca8d2b-6440-4034-bfed-f447a354be80; _madid=60ef714a-e558-4bd8-b224-4afe8c40f2b3; csrf-token-cookie=0cofZYfGKHHDYqD9AuQjGg2u4OSsHLzpwlYtSL5QrWBVHj-1CH1cGWQyOvlGWQMra9g0GyaiLdx951gO_stQvLlQ-Mw1; ARRAffinity=7f6dab0e5dcfecf45a1fc2e4afee9022579797bcb025c2a3e0d18213c97fe658; ARRAffinitySameSite=7f6dab0e5dcfecf45a1fc2e4afee9022579797bcb025c2a3e0d18213c97fe658; CIConsentStatistic=true; _gid=GA1.2.209746787.1615446928; 100148hideNotificationBlock=true; __RequestVerificationToken=QBTT6PfhEcrfjcpwEcXet3Voe-CL9dQtiwwetgVY3VBjiFP6sRcd3JtiE3q9U-k11OyYrUvL8p6J7Dq2WGl_4QuKY6s1; is=3e794e1a-cb85-4628-b1cd-d010d0540da6; iv=d05dde81-4ce9-46a1-9815-a1295dd41174; _ga=GA1.2.36147646.1615206183; _uetsid=8ecb6410823911eba3f915e759fd9251; _uetvid=0762d020800911eb8faff5aa7b0dfa6f; ai_session=NjNrX|1615446928698|1615447032913.8; _ga_MXK038GCNF=GS1.1.1615446928.2.1.1615447040.8; __cfduid=de135673fe969d1230b1d26d16a89c15f1615446940; EPiSessionId=c2ca8d2b-6440-4034-bfed-f447a354be80'
# }
#
#
# class AlmSpider(scrapy.Spider):
#     name = 'alm'
#     start_urls = ['https://www.almbrand.dk/om-alm-brand/presse/nyhed/']
#     base_url = 'https://www.almbrand.dk'
#     def parse(self, response):
#
#         data = requests.request("GET", url, headers=headers, data=payload)
#         data = json.loads(data.text)
#
#         for index in range(len(data['newsItems'])):
#             for key in range(len(data['newsItems'][index])):
#                 link = data['newsItems'][index][key]['url']
#                 full_url = self.base_url + link
#                 yield response.follow(full_url, self.parse_post)
#
#         for page in data['pages']:
#             requests.request("GET", url, headers=headers, data=payload,callback=self.parse)
#
#     def parse_post(self, response):
#         date = response.xpath('//div[@class="grid-2-3 manchet centercontent datestyle"]/p/span[last()]/text()').get()
#         date = re.findall(r'\w+\s\d+\,\s\d+',date)
#         title = response.xpath('//div[@class="grid-2-3 centercontent"]/h3/text()').get()
#         content = response.xpath('(//div[@class="grid-2-3 centercontent"])[position()>2]//text()').getall()
#         content = [p.strip() for p in content if p.strip()]
#         content = re.sub(pattern, "",' '.join(content))
#
#         item = ItemLoader(item=AlmItem(), response=response)
#         item.default_output_processor = TakeFirst()
#
#         item.add_value('title', title)
#         item.add_value('link', response.url)
#         item.add_value('content', content)
#         item.add_value('date', date)
#
#         yield item.load_item()
