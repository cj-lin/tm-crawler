from urllib.parse import parse_qs, urlparse

import scrapy
from lxml import etree


class D67OfficerSpider(scrapy.Spider):
    name = "d67officer"
    allowed_domains = ["www.toastmasters.org.tw"]
    start_urls = list(
        map(
            lambda x: f"https://www.toastmasters.org.tw/page.php?page_type=division&division={x}&mode=&ver=en",
            ["d67", "PQD", "CGD", "PR"] + list(map(chr, range(ord("A"), ord("Q")))),
        )
    )

    def get_xpath(self, response, xpath):
        return list(map(lambda x: " ".join(x.split()), response.xpath(xpath).getall()))

    def extract(self, inner):
        cname = ename = title = telephone = email = ""
        for i, li in enumerate(
            etree.fromstring(inner, parser=etree.XMLParser(recover=True))
        ):
            if "class" in li.attrib:
                if li.attrib["class"] == "name":
                    if len(li) == 1:
                        name = li[0].tail.strip().replace(" ", " ")
                        if name.isascii():
                            ename = name
                        else:
                            cname = name
                    else:
                        cname = li[0].tail.strip().replace(" ", " ")
                        ename = li[1].text.strip().replace(" ", " ")
                elif li.attrib["class"] == "telephone":
                    telephone = li.text
            elif i == 1:
                title = li.text.strip()
            else:
                for letter in li[0].text.split('"')[1]:
                    if letter.isalpha():
                        stayInAlphabet = ord(letter) + 13
                        if stayInAlphabet > ord("z"):
                            stayInAlphabet -= 26
                        email += chr(stayInAlphabet)
                    else:
                        email += letter
        return cname, ename, title, telephone, email

    def parse(self, response):
        page = parse_qs(urlparse(response.url).query)["division"][0]
        imgs = self.get_xpath(response, "//div[@class='member-portrait']/img/@src")
        position_cs = self.get_xpath(response, "//li[@class='position_c']/text()")
        position_es = self.get_xpath(response, "//li[@class='position_e']/text()")
        inners = self.get_xpath(response, "//div[@class='team-member-inner-2']")

        for img, position_c, position_e, inner in zip(
            imgs, position_cs, position_es, inners
        ):
            cname, ename, title, telephone, email = self.extract(inner)
            yield {
                "page": page,
                "img": img,
                "position_c": position_c,
                "position_e": position_e,
                "cname": cname,
                "ename": ename,
                "title": title,
                "telephone": telephone,
                "email": email,
            }
