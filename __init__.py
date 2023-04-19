import time

from Downloader import Downloader
from parse import Parser, Pages
import data

def process(url, file_path="untitled.txt", result_path="result.csv", params = None):

    downloader = Downloader(URL)
    downloader.save(FILE_PATH)

    final = []
    Page = Pages(50)

    for urll in Page:

        d = Downloader(urll, method="GET")
        p = Parser(urll)
        d.save("untitled.txt")
        while (True):
            try:
                final += p.parse(urll)
            except:
                time.sleep(1)
            else:
                break
    res = open('result.csv', 'w+')
    res.write('name,year,price,liters,horse_power,type,another_type,engine' + '\n')
    res.write(final[0])
    for i in final[1:]:

        res.write('\n' + i)




URL = 'https://auto.drom.ru/bmw/new/all/page0/?fueltype=1&unsold=1'
FILE_PATH = "untitled.txt"
PARSED_FILE_PATH = "result.csv"

process(URL, FILE_PATH, PARSED_FILE_PATH)
data.show_analyt()



