import scrapy
from scrapy.selector import Selector
import csv


class CursosListSpider(scrapy.Spider):
    name = "cursos-list"
    file_header = ["curso", "code", "url"]

    def start_requests(self):
        urls = [
            'http://opencampus.utpl.edu.ec/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        cursos_list_raw = response.selector.xpath("//li[@class='courses-listing-item']").getall()
        cursos_list = []
        for curso in cursos_list_raw:
            url = Selector(text=curso).xpath('//article/a/@href').get()
            code = Selector(text=curso).xpath('//article/a/div/h2/span[@class="course-code"]/text()').get()
            curso = Selector(text=curso).xpath('//article/a/div/h2/span[@class="course-title"]/text()').get()
            cursos_list.append({
                "url": url,
                "code": code,
                "curso": curso,
            })
        with open("./cursos-raw.csv", mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.file_header, delimiter=',')
            writer.writeheader()

            writer.writerows(cursos_list)
            f.close()
