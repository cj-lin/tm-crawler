import scrapy


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
        get = response.xpath(xpath).get()
        return get.strip() if get else None

    def parse(self, response):
        return {
            "title": self.get_xpath(response, "/html/body/div[1]/h2/text()"),
            "description": self.get_xpath(response, "/html/body/div[1]/p[1]/text()"),
            "purpose": self.get_xpath(response, "/html/body/div[1]/p[2]/text()[2]"),
            "overview": self.get_xpath(response, "/html/body/div[1]/p[3]/text()[2]"),
            "includes1": self.get_xpath(response, "/html/body/div[1]/p[4]/text()[2]"),
            "includes2": self.get_xpath(response, "/html/body/div[1]/p[4]/text()[3]"),
            "includes3": self.get_xpath(response, "/html/body/div[1]/p[4]/text()[4]"),
            "includes4": self.get_xpath(response, "/html/body/div[1]/p[4]/text()[5]"),
            "includes5": self.get_xpath(response, "/html/body/div[1]/p[4]/text()[6]"),
            "form1": self.get_xpath(response, "/html/body/div[2]/a[2]/@href"),
            "form2": self.get_xpath(response, "/html/body/div[2]/a[3]/@href"),
            "form3": self.get_xpath(response, "/html/body/div[2]/a[4]/@href"),
        }
