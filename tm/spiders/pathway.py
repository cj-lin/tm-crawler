from urllib.parse import parse_qs, urlparse

import scrapy
from lxml import etree


class PathwaySpider(scrapy.Spider):
    name = "pathway"
    allowed_domains = ["ckc300.neocities.org"]
    start_urls = list(
        map(
            lambda x: f"https://ckc300.neocities.org/{x}.html",
            [
                "8101",
                "8100",
                "8102",
                "8207",
                "8206",
                "8204",
                "8205",
                "8202",
                "8200",
                "8201",
                "8203",
                "8208",
                "8307",
                "8313",
                "8320",
                "8312",
                "8309",
                "8316",
                "8315",
                "8308",
                "8314",
                "8303",
                "8306",
                "8300",
                "8301",
                "8302",
                "8304",
                "8305",
                "8310",
                "8317",
                "8318",
                "8319",
                "8406",
                "8403",
                "8415",
                "8405",
                "8411",
                "8404",
                "8401",
                "8408",
                "8409",
                "8412",
                "8400",
                "8402",
                "8407",
                "8413",
                "8414",
                "8504",
                "8512",
                "8507",
                "8511",
                "8501",
                "8503",
                "8509",
                "8505",
                "8502",
                "8506",
                "8508",
                "8510",
            ],
        )
    )

    def get_xpath(self, response, xpath):
        return list(map(lambda x: " ".join(x.split()), response.xpath(xpath).getall()))

    def parse(self, response):
        return {
            "title": response.xpath("/html/body/div[1]/h2/text()").get(),
            "description": response.xpath("/html/body/div[1]/p[1]/text()").get(),
            "purpose": response.xpath("/html/body/div[1]/p[2]/text()[2]").get(),
            "overview": response.xpath("/html/body/div[1]/p[3]/text()[2]").get(),
            "includes1": response.xpath("/html/body/div[1]/p[4]/text()[2]").get(),
            "includes2": response.xpath("/html/body/div[1]/p[5]/text()").get(),
            "includes3": response.xpath("/html/body/div[1]/p[6]/text()").get(),
            "includes4": response.xpath("/html/body/div[1]/p[7]/text()").get(),
            "includes5": response.xpath("/html/body/div[1]/p[8]/text()").get(),
            "form1": response.xpath("/html/body/div[2]/a[2]/@href").get(),
            "form2": response.xpath("/html/body/div[2]/a[3]/@href").get(),
            "form3": response.xpath("/html/body/div[2]/a[4]/@href").get(),
        }
