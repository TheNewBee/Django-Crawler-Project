# -*- coding: utf-8 -*-

import base64
import re
import time
import sys
import urlparse
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_v1_5
from django.http import HttpResponse
from passlib.hash import argon2
from MainModel.models import SchoolGooglePlaceid, Member, School, SchoolApplyNumber, SchoolRelateLocation, Loaction

reload(sys)
sys.setdefaultencoding('utf-8')

def getschoolplaceid(id):
    if id > 0:
        query = 'SELECT sgp.* FROM school_google_placeid sgp NATURAL JOIN school s WHERE s.Location_ID=' + id
        return SchoolGooglePlaceid.objects.using('main').raw(query)
    return SchoolGooglePlaceid.objects.using('main').all()

def register(usernameinput, passwordinput, emailinput):
    usernameinput = usernameinput.strip()
    passwordinput = passwordinput.strip()
    emailinput = emailinput.strip()

    if not (usernameinput and passwordinput and emailinput) \
        or len(usernameinput) < 3 or len(usernameinput) > 30 \
        or not re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', emailinput):
        return -1

    list = Member.objects.using('main').filter(username=usernameinput)
    if list.count() > 0:
        return -2

    passwordinput = decrypt(passwordinput)
    passwordinput = argon2.using(rounds=10, memory_cost=128, max_threads=1).hash(passwordinput)
    try:
        member = Member(
            username = usernameinput,
            password = passwordinput,
            email = emailinput,
            memberlevel = 1,
            regdate = time.time(),
            lastlogin = 0.0,
            blocked = 0,
            activated = 0)
        member.save(using='main')
    except:
        return 0
    return 1

def login(usernameinput, passwordinput):
    usernameinput = usernameinput.strip()
    passwordinput = passwordinput.strip()

    if not (usernameinput and passwordinput):
        return -1

    passwordinput = decrypt(passwordinput)
    list = Member.objects.using('main').filter(username=usernameinput)
    if list.count() == 1:
        if argon2.verify(passwordinput, list[0].password):
            return 1
        else:
            return -2
    else:
        return -3
    return 0

def decrypt(data):
    data = urlparse.unquote(data)
    data = base64.b64decode(data)
    secret_code = "5kxLHGYgCsycenAkGxB4ssC63UtFmWzhh5VE2uJuMyqAQ7LmLK75amejeFreLM4T"
    encoded_key = open("/root/Raymond/private_rsa_key.bin", "rb").read()
    private_key = RSA.import_key(encoded_key, passphrase=secret_code)
    cipher_rsa = PKCS1_v1_5.new(private_key)
    decoded_data = cipher_rsa.decrypt(data, None)
    return decoded_data

def getlocationbyid(id):
    if str(id).isdigit():
        list = Loaction.objects.using('main').filter(location_id=id)
        if list.count() > 0:
            return list[0].location
    return ''

def getschoolsbylocationid(id):
    list = {}
    if str(id).isdigit():
        list = School.objects.using('main').filter(location_id=id)
    return list

def getschoolsbyschoolid(id):
    list = {}
    if str(id).isdigit():
        list = School.objects.using('main').filter(school_id=id)
        if len(list) == 1:
            return list[0]
    return None

def getschoolsformap():
    list = {}
    list = School.objects.using('main').all()
    return list

# King
#
def getallschools(context):
    list = School.objects.using('main').filter(school_id=1) # "SELECT * FROM school WHERE School_ID"
    if list.count() > 0:
        return list
    else:
        return list
    return {}
