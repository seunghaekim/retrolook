from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.shortcuts import render
from rawdata.models import Rawdata
from .crawler import Crawler
import datetime
import time
import re


def index(request):
    return HttpResponse('hello world')


def latestCrawled(request):
    lists = Rawdata.objects.all()
    context = {
        'message': 'Total count of Crawled documents is %d' % lists.count(),
        'lists': lists.order_by('-createtime')[:10]
    }

    return render(request, 'rawdata/list.html', context)


def crawler():
    crawler = Crawler()
    for year in crawler.collectYears():
        print('%s %s' % (datetime.datetime.now(), year))
        for month in crawler.collectMonths(year):
            print('%s %s' % (datetime.datetime.now(), month))
            for day in crawler.collectDays(month):
                if Rawdata.objects.filter(uri=day).count() > 0:
                    continue
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
