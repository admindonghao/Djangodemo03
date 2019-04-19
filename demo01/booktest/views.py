from django.shortcuts import render
from .models import BookInfo,HeroInfo
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.
def index(requset):
    return render(requset, 'booktest/index.html', {})


def list(requset):
    books = BookInfo.objects.all()
    return render(requset, 'booktest/list.html', {'booklist':books})


def detail(requset, id):
    book = BookInfo.objects.get(pk = id)
    return render(requset, 'booktest/detail.html', {'book':book})
