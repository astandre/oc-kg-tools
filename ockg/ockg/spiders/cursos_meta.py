import scrapy
from scrapy.selector import Selector
import csv
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Text, Integer
from sqlalchemy.ext.declarative import declarative_base

engine = db.create_engine('sqlite:///rawcursos.sqlite')

Base = declarative_base()


class Raw(Base):
    __tablename__ = 'rawcursos'
    id = Column(Integer, primary_key=True)
    curso = Column(String(200), nullable=False)
    url = Column(String(200), nullable=False)
    raw = Column(Text, nullable=False)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


class CursosMetaSpider(scrapy.Spider):
    name = "cursos-meta"
    BASE_URL = 'http://opencampus.utpl.edu.ec'
    cont = 0
    cursos_list = []

    def start_requests(self):

        with open("./cursos-raw.csv", mode='r', encoding='utf-8') as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                row["url"] = f"{self.BASE_URL}{row['url']}"
                self.cursos_list.append({
                    "url": row["url"],
                    "code": row["code"],
                    "curso": row["curso"],
                })

        # print(cursos_list)
        for url in self.cursos_list:
            yield scrapy.Request(url=url["url"], callback=self.parse, meta={'cont': self.cont})
            self.cont += 1

    def parse(self, response):
        raw = response.selector.xpath("//section[@class='container']").get()
        session.add(Raw(curso=self.cursos_list[response.meta["cont"]]["curso"], url=response.url, raw=raw))
        session.commit()
