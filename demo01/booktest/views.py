from django.shortcuts import render
from .models import BookInfo,HeroInfo
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.


# 首页视图函数
def index(requset):
    return render(requset, 'booktest/index.html', {})


# 列表页视图函数
def list(requset):
    books = BookInfo.objects.all()
    return render(requset, 'booktest/list.html', {'booklist':books})


# 详情页视图函数
def detail(requset, id):
    book = BookInfo.objects.get(pk = id)
    return render(requset, 'booktest/detail.html', {'book':book})


# 删除图书视图函数
def deletebook(requset, id):
    BookInfo.objects.get(pk=id).delete()
    return HttpResponseRedirect('/booktest/list/')



def deletehero(requset, id):
    HeroInfo.objects.get(pk=id).delete()
    return HttpResponseRedirect('/booktest/list/')


# 添加的视图函数
def addbook(requset):
    return render(requset, 'booktest/addbook.html', {})


def addbooks(requset):
    b = BookInfo()
    b.btitle = requset.POST['btitle']
    b.save()
    return HttpResponseRedirect('/booktest/list/')


# 更新英雄信息
def update(requset, id):
    hero = HeroInfo.objects.get(pk=id)
    return render(requset, 'booktest/update.html', {'hero':hero})


def updates(requset, id):
    h = HeroInfo.objects.get(pk=id)
    h.hname = requset.POST['name']
    h.hgender = requset.POST['gender']
    h.hconent = requset.POST['conent']
    h.save()
    return HttpResponseRedirect('/booktest/list/')


def create(requset, id):
    book = BookInfo.objects.get(pk=id)
    return render(requset, 'booktest/create.html', {'book':book})


def creates(requset,id):
    h = HeroInfo()
    h.hname = requset.POST['name']
    h.hgender = requset.POST['gender']
    h.hconent = requset.POST['conent']
    h.hbook = BookInfo.objects.get(pk=id)
    h.save()
    return HttpResponseRedirect('/booktest/list/')
