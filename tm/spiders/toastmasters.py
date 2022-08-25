import itertools
from urllib.parse import parse_qs, urlparse

import scrapy


class ToastmastersSpider(scrapy.Spider):
    name = "toastmasters"
    allowed_domains = ["www.toastmasters.org.tw"]
    start_urls = list(
        map(
            lambda x: f"https://www.toastmasters.org.tw/page.php?page_type=division&division={x}&mode=&ver=en",
            ["d67", "PQD", "CGD", "PR"] + list(map(chr, range(ord("A"), ord("Q")))),
        )
    )

    def get(self, response, xpath):
        return list(map(lambda x: x.strip(), response.xpath(xpath).getall()))

    def parse(self, response):
        page = parse_qs(urlparse(response.url).query)["division"][0]
        img = self.get(response, "//div[@class='member-portrait']/img/@src")
        position_e = self.get(response, "//li[@class='position_e']/text()")
        cname = self.get(response, "//li[@class='name']/text()[1]")
        ename = self.get(response, "//li[@class='name']/text()[2]")
        title = self.get(response, "//div[@class='team-member-inner-2']/li[2]/text()")
        telephone = self.get(response, "//li[@class='telephone']/text()")

        ename = map(lambda x: x.replace(" ", " "), ename)

        for data in itertools.zip_longest(
            img, position_e, cname, ename, title, telephone
        ):
            TMItem = {
                "page": page,
                "img": data[0],
                "position_e": data[1],
                "cname": data[2],
                "ename": data[3],
                "title": data[4],
                "telephone": data[5],
            }
            yield TMItem
