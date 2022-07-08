from django.db import models


# Create your models here.
class douluo(models.Model):
    title = models.CharField(verbose_name="标题", max_length=64)
    content = models.TextField(verbose_name="正文")
    link = models.CharField(verbose_name="链接", max_length=64)


class tsxk(models.Model):
    title = models.CharField(verbose_name="标题", max_length=64)
    content = models.TextField(verbose_name="正文")
    link = models.CharField(verbose_name="链接", max_length=64)
