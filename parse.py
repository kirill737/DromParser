import time

from Downloader import Downloader
import math
from bs4 import BeautifulSoup



#Перелистывание страниц
links=[]


def Pages(a):
    count=math.ceil(a/20)
    for i in range(count):
        link="https://auto.drom.ru/bmw/new/all/page{0}/?fueltype=1&unsold=1".format(i)
        links.append(link)
    return links

class Parser():
    def __init__(self,link):
        self.link=link
    def parse(self,link):
        f=open('untitled.txt')
        bs = BeautifulSoup(f.read(),"lxml")

        # Литры,топливо,коробка,wd
        engine = ""
        temp = bs.find('span','css-1l9tp44 e162wx9x0')
        engine += temp.text.replace(',', '')
        var = temp.find_all_next('span','css-1l9tp44 e162wx9x0')

        #Разбиваем по 4
        count = 1
        for el in var:
            tmp = el.text.replace(',', '')
            engine = engine + ', ' + tmp
            count += 1
            if count == 4:
                count = 0
                engine += '|'

        info = engine.split('|, ')
        info[-1] = info[-1].replace('|', '')

        # Название год
        Name = ""
        name = bs.find('div','css-l1wt7n e3f4v4l2')
        Name += name.text + ","
        names = name.find_all_next('div','css-l1wt7n e3f4v4l2')
        count = 0
        for nm in names:
            Name = Name + nm.text + ","

        # Цена
        Prices = ""
        price = bs.find('span', 'css-46itwz e162wx9x0')
        Prices += price.text[:-1] + ","
        prices = price.find_all_next('span', 'css-46itwz e162wx9x0')
        for nm in prices:
            Prices = Prices + nm.text[:-1] + ","

        # Удаление лишних символов из инфы про цену
        TruePrice = ""
        for i in Prices.split(' '):
            TruePrice += i.replace('\xa0', '')
        TruePrice = TruePrice.split(',')
        TruePrice = TruePrice[:-1]

        tmp = []
        name = []
        count = 0
        for i in Name.split(','):
            tmp.append(i)
            count += 1
            if count == 2:
                name.append(tmp)
                tmp = []
                count = 0

        # Удаление лишних символов из инфы про двигатель
        count = 0
        for i in range(len(info)):
            count += 1
            info[i] = info[i].replace(' ', '').split(',')
            if str(info[i][0]).find('л') == -1:
                print(info)
                info = info[:-len(info) + count]
                print(info)
                break


        for i in range(len(info)):
            tmp = info[i][0].replace('л.с.)', '').replace('л', '').split('(')

            info[i][0] = tmp[0] + ',' + tmp[1]


        # Формируем конечный список строк
        final =[]
        for i in range(len(TruePrice)):

            tmp = str(name[i][0]) + ',' + str(name[i][1].replace(' ', '')) + ',' + str(TruePrice[i])
            for j in info[i]:
                tmp += ',' + str(j)
                pass
            final.append(tmp)

        # Вывод для тестов
        # print('Кол-во инфы про двигатель: ' + str(len(info)))
        # print('Кол-во названий: ' + str(len(name)))
        # print('Кол-во цен: ' + str(len(TruePrice)))

        # Вывод все строк для анализа
        # for i in final:
        #     print(i)

        return final














