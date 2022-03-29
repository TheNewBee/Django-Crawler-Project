# -*- coding: utf-8 -*-

import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
from . import maindb

def schoolmap(request):
    context = {}
    schools = maindb.getschoolsformap()
    context['schools'] = schools
    if request.GET:
        try:
            district_id = request.GET['district_id']
            district = maindb.getlocationbyid(district_id)
            schools = maindb.getschoolsbylocationid(district_id)
            context['schools'] = schools
            context['district_id_uri'] = "?district_id=" + district_id
        except:
            None
    return render(request, "school-map.html", context)

def functions_getSchoolDetails(request):
    context = {}
    context['result'] = 'error'
    if request.GET:
        school_id = request.GET['school_id']
        school = maindb.getschoolsbyschoolid(school_id)
        if school is not None:
            context['result'] = 'success'
            data = {}
            data['school_id'] = school.school_id
            data['school_name'] = school.school_name
            data['school_address'] = school.school_address
            data['telephone'] = school.telephone
            data['fax'] = school.fax
            data['supervisor_or_chairman'] = school.supervisor_or_chairman
            data['school_head'] = school.school_head
            data['email'] = school.email
            data['website'] = school.website
            data['school_photo'] = school.school_photo
            data['facility'] = school.facility
            data['motto'] = school.motto
            data['mission'] = school.mission
            data['development_key'] = school.development_key
            data['subject_by_chinese'] = school.subject_by_chinese
            data['subject_by_english'] = school.subject_by_english
            data['location_id'] = school.location_id
            data['funding_type_id'] = school.funding_type_id
            data['school_net_id'] = school.school_net_id
            data['day_type_id'] = school.day_type_id
            data['student_gender_id'] = school.student_gender_id
            data['education_type_id'] = school.education_type_id
            data['religion_id'] = school.religion_id
            data['total_teacher'] = school.total_teacher
            data['teacher_diploma'] = school.teacher_diploma
            data['teacher_bachelor'] = school.teacher_bachelor
            data['teacher_master_above'] = school.teacher_master_above
            data['teacher_04year'] = school.teacher_04year
            data['teacher_59year'] = school.teacher_59year
            data['teacher_10year_above'] = school.teacher_10year_above
            data['banding'] = school.banding
            data['percentageof3322in4'] = school.percentageof3322in4
            data['lv3chinese'] = school.lv3chinese
            data['lv3english'] = school.lv3english
            data['percentagetouni'] = school.percentagetouni
            data['percentageof14markin6'] = school.percentageof14markin6
            data['boyathleticrank'] = school.boyathleticrank
            data['girlathleticrank'] = school.girlathleticrank
            data['boyftballrank'] = school.boyftballrank
            data['girlftballrank'] = school.girlftballrank
            data['boyswimrank'] = school.boyswimrank
            data['girlswimrank'] = school.girlswimrank
            data['boybasketrank'] = school.boybasketrank
            data['girlbasketrank'] = school.girlbasketrank
            data['ntboyrank'] = school.ntboyrank
            data['ntgirlrank'] = school.ntgirlrank
            data['musicfirst'] = school.musicfirst
            data['musicsecond'] = school.musicsecond
            data['musicthird'] = school.musicthird
            data['speechfirst'] = school.speechfirst
            data['speechsecond'] = school.speechsecond
            data['speechthird'] = school.speechthird
            data['other_music'] = school.other_music
            context['data'] = data
    return HttpResponse(json.dumps(context), content_type="application/json")

def functions_schoolmap(request):
    context = {}
    if request.GET:
        try:
            district_id = request.GET['district_id']
            context['district_id_uri'] = "?district_id=" + district_id
        except:
            None
    return render(request, 'functions/schoolmap2.html', context)

def functions_schoolmapxml(request):
    response = ""
    list = maindb.getschoolplaceid(0)
    if request.GET:
        try:
            district_id = request.GET['district_id']
            list = maindb.getschoolplaceid(district_id)
        except:
            None
    for var in list:
        response += '<marker '
        response += 'schoolid="' + str(var.school_id) + '" '
        response += 'placeid="' + str(var.google_place_id) + '" '
        response += 'name="' + str(var.name) + '" '
        response += 'address="' + str(var.address) + '" '
        response += 'lat="' + str(var.geometry_lat) + '" '
        response += 'lng="' + str(var.geometry_lng) + '" '
        response += '/>'
    if response is not "":
        return HttpResponse("<markers>" + response + "</markers>", content_type='text/xml')
    else:
        return HttpResponse("", content_type='text/xml')

def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__,
        sort_keys=True, indent=4)
