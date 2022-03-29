# -*- coding: utf-8 -*-

from Crypto.PublicKey import RSA
from django.shortcuts import render
from django.views.decorators import csrf
from . import maindb

def register(request):
    context = {}
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        context['status'] = maindb.register(username, password, email)
    else:
        key = RSA.import_key(open("/root/Raymond/public_key.pem").read())
        context['public_key'] = key.publickey().exportKey()
    return render(request, "register.html", context)

def login(request):
    context = {}
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        context['status'] = maindb.login(username, password)
    else:
        key = RSA.import_key(open("/root/Raymond/public_key.pem").read())
        context['public_key'] = key.publickey().exportKey()
    return render(request, "login.html", context)

def test(request):
    context = {}
    key = RSA.import_key(open("/root/Raymond/public_key.pem").read())
    context['public_key'] = key.publickey().exportKey()
    return render(request, "encrypttest.html", context)
