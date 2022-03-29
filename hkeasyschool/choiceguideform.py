# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf
from . import maindb

def formsubmit(request):
    context = {}
    result = {}
    if request.GET:
        context['sex'] = request.GET['sex']
        context['location'] = request.GET['menu1']
        context['live_id'] = request.GET["live_id"]
        context['avgMark'] = request.GET["avgMark"]
        context['rate1'] = request.GET["rate1"]
        context['rate2'] = request.GET["rate2"]
        context['rate3'] = request.GET["rate3"]
        context['rate4'] = request.GET["rate4"]
        context['inputWantSch1'] = request.GET["inputWantSch1"]
        context['inputWantSch2'] = request.GET["inputWantSch2"]
        context['inputWantSch3'] = request.GET["inputWantSch3"]
        context['religion'] = request.GET["menu4"]

        result = maindb.getallschools(context)
    return render(request, "form.html", context)
