from rest_framework.cctv_prediction.common.abstracts import PrinterBase, ReaderBase, ScraperBase
import pandas as pd
import json
import googlemaps
from selenium import webdriver


class Printer(PrinterBase):

    def dframe(self, this):

        n = 10
        print('*' * 100)
        print(f'1. Target 의 Type 은 {type(this)}')
        print(f'2. Target 의 column 은 {this.columns}')
        print(f'3. Target 의 상위 {n}개 행은 \n{this.head(n)}')
        print(f'4. Target null 의 개수 \n{this.isnull().sum()}개')


class Reader(ReaderBase):
    def new_file(self, file) -> str:
        return file.context + file.fname

    def csv(self, file) -> object:
        return pd.read_csv(f'{self.new_file(file)}.csv', encoding='UTF-8', thousands=',')

    def xls(self, file, header, usecols) -> object:
        return pd.read_excel(f'{self.new_file(file)}.xls', header=header, usecols=usecols)

    def json(self, file) -> object:
        return json.load(open(f'{self.new_file(file)}.json', encoding='UTF-8'))

    def gmaps(self) -> object:
        return googlemaps.Client(key='')


class Scraper(ScraperBase):

    def driver(self) -> object:
        return webdriver.Chrome('C:/Program Files/Google/Chrome/chromedriver')

    def auto_login(self):
        pass
