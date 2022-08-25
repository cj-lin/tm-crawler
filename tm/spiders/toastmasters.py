import itertools

import scrapy


class ToastmastersSpider(scrapy.Spider):
    name = "toastmasters"
    allowed_domains = ["www.toastmasters.org.tw"]
    start_urls = [
        "https://www.toastmasters.org.tw/page.php?page_type=division&division=D67&mode=&ver=en"
    ]

    def get(self, response, xpath):
        return list(
            filter(str, map(lambda x: x.strip(), response.xpath(xpath).getall()))
        )

    def parse(self, response):
        img = self.get(response, "//div[@class='member-portrait']/img/@src")
        position_e = self.get(response, "//li[@class='position_e']/text()")
        name = self.get(response, "//li[@class='name']/text()")
        title = self.get(response, "//div[@class='team-member-inner-2']/li[2]/text()")
        telephone = self.get(response, "//li[@class='telephone']/text()")

        name = map(lambda x: x.replace(" ", " "), name)

        for data in itertools.zip_longest(img, position_e, name, title, telephone):
            TMItem = {
                "img": data[0],
                "position_e": data[1],
                "name": data[2],
                "title": data[3],
                "telephone": data[4],
            }
            yield TMItem
