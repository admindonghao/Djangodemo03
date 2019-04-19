from django.db import models


# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.btitle

    def name(self):
        return self.btitle
    name.short_description = '书籍名称'


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.CharField(max_length=10)
    hconent = models.CharField(max_length=50)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    def __str__(self):
        return self.hname

    def name(self):
        return self.hname
    name.short_description = '人物'

    def book(self):
        return self.hbook
    book.short_description = '所属书籍'
