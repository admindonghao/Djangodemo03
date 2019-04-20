from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import IssueList,ChioceList


# Create your views here.
def index(requset):
    return render(requset, 'polls/index.html', {})


def list(requset):
    pl = IssueList.objects.all()
    print(pl)
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
