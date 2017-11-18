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
    print('collect years start')
    years = [year for year in crawler.collectYears()]
    print('%s collect years done' % datetime.datetime.now())
    print('%s collect months start' % datetime.datetime.now())
    months = [month for year in list(map(lambda y: crawler.collectMonths(y), years)) for month in year]
    print('%s collect months done' % datetime.datetime.now())
    print('%s collect days start' % datetime.datetime.now())
    days = [day for month in list(map(lambda m: crawler.collectDays(m), months)) for day in month]
    print('%s collect days done' % datetime.datetime.now())
    for day in days:
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
        if Rawdata.objects.filter(url=day).count() < 1:
            rawdata = Rawdata(
                document=str(crawler.collectContent(day)),
                uri=day,
                createtime=datetime.datetime.now(),
                pubtime=time.strftime('%Y-%m-%d', time.strptime(
                        re.compile(r'[^\d]').sub('', day.split('/')[-1]), '%Y%m%d'
                )),
                origin='neolook'
            )
            rawdata.save()
            print('%s %s' % (datetime.datetime.now(), rawdata.uri))

    return None
