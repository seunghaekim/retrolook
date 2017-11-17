from django.db import models


class Rawdata(models.Model):
    document = models.TextField()
    uri = models.CharField(max_length=50)
    createtime = models.DateTimeField()
    pubtime = models.DateField()
    origin = models.SlugField(default='neolook')
