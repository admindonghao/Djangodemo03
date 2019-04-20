from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import IssueList,ChioceList


# Create your views here.
def index(requset):
    return render(requset, 'polls/index.html', {})


def list(requset):
    pl = IssueList.objects.all()
    # print(pl)
    return render(requset, 'polls/list.html', {'polls':pl})


def detail(request, id):
    poll = IssueList.objects.get(pk=id)
    return render(request, 'polls/detail.html', {'poll':poll})


def details(request, id):
    poll = IssueList.objects.get(pk=id)
    po = request.POST['poll']
    cho = ChioceList.objects.get(pk=po)
    cho.number += 1
    cho.save()
    return render(request, 'polls/details.html', {'poll':poll})


def deleteiss(request, id):
    IssueList.objects.get(pk=id).delete()
    return HttpResponseRedirect('/polls/list/')


def deletec(request, id):
    c = ChioceList.objects.get(pk=id)
    c.delete()
    # print(c.is_issue.id)
    return HttpResponseRedirect('/polls/detail/{}/'.format(c.is_issue.id))


def update(requset, id):
    iss = IssueList.objects.get(pk=id)
    return render(requset, 'polls/update.html', {'iss':iss})


def updates(requset, id):
    i = IssueList.objects.get(pk=id)
    i.issue = requset.POST['issue']
    i.save()
    return HttpResponseRedirect('/polls/list/')


def addw(requset):
    return render(requset, 'polls/addw.html', {})


def addws(requset):
    i = IssueList()
    i.issue = requset.POST['wen']
    i.save()
    return HttpResponseRedirect('/polls/list/')


def createch(requset, id):
    iss = IssueList.objects.get(pk=id)
    return render(requset, 'polls/create.html', {'iss':iss})


def createchs(requset,id):
    i = IssueList.objects.get(pk=id)
    c = ChioceList()
    c.options = requset.POST['option']
    c.is_issue = i
    c.save()
    return HttpResponseRedirect('/polls/detail/{}/'.format(id))


def result(request):
    cl = ChioceList.objects.all()
    return render(request, 'polls/result.html', {'cl':cl})