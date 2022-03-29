# from django.http import HttpResponse
from django.shortcuts import render
from . import maindb


def index(request):
    context = {}
    return render(request, 'main.html', context)


def login(request):
    context = {}
    return render(request, 'login.html', context)


def register(request):
    context = {}
    return render(request, 'register.html', context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context)


def school_news(request):
    context = {}
    return render(request, 'school-news.html', context)


def school_ranking(request):
    context = {}
    return render(request, 'school-ranking.html', context)


def school_info(request):
    context = {}
    return render(request, 'school-info.html', context)


def choice_guide(request):
    context = {}
    return render(request, 'choice-guide.html', context)
