from django.shortcuts import render
from django.http import HttpResponse
from .crawler import Crawler
import datetime
import time
import re
from rawdata.models import Rawdata
from django.utils import timezone


def index(request):
    return HttpResponse('hello world')


def crawler():
    crawler = Crawler()
    years = [year for year in crawler.collectYears()]
    months = [month for year in list(map(lambda y: crawler.collectMonths(y), years)) for month in year]
    days = [day for month in list(map(lambda m: crawler.collectDays(m), months)) for day in month]
    for day in days[:1]:
        data = {
            'document': crawler.collectContent(day),
            'uri': day,
            'createtime': datetime.datetime.now(),
            'pubtime': time.strftime(
                '%Y-%m-%d',
                time.strptime(
                    re.compile(r'[^\d]').sub('', day.split('/')[-1]),
                    '%Y%m%d'
                )
            )
        }
        rawdata = Rawdata(
            document=crawler.collectContent(day),
            uri=day,
            createtime=datetime.datetime.now(),
            pubtime=time.strftime('%Y-%m-%d', time.strptime(
                    re.compile(r'[^\d]').sub('', day.split('/')[-1]), '%Y%m%d'
            )),
            origin='neolook'
        )
        rawdata.save()
        print(rawdata.uri)

    # for month in crawler.collectMonths(year):
    #     for day in crawler.collectDays(month):
    #         data = {
    #             'document': crawler.collectContent(day),
    #             'uri': day,
    #             'createtime': datetime.datetime.now(),
    #             'pubtime': time.strftime(
    #                 '%Y-%m-%d',
    #                 time.strptime(
    #                     re.compile(r'[^\d]').sub('', day.split('/')[-1]),
    #                     '%Y%m%d'
    #                 )
    #             )
    #         }
    #
    #         print(data['pubtime'])

    return HttpResponse('aaa')
