# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DayType(models.Model):
    day_type_id = models.AutoField(db_column='Day_Type_ID', primary_key=True)  # Field name made lowercase.
    day_type = models.CharField(db_column='Day_Type', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'day_type'


class EducationType(models.Model):
    education_type_id = models.AutoField(db_column='Education_Type_ID', primary_key=True)  # Field name made lowercase.
    education_type = models.CharField(db_column='Education_Type', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'education_type'


class EventInfo(models.Model):
    event_id = models.AutoField(db_column='Event_ID', primary_key=True)  # Field name made lowercase.
    start_date = models.DateField(db_column='Start_Date', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateField(db_column='End_Date', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=150, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    event_type = models.IntegerField(db_column='Event_Type', blank=True, null=True)  # Field name made lowercase.
    link = models.CharField(db_column='Link', max_length=400, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'event_info'


class EventType(models.Model):
    event_type_id = models.IntegerField(primary_key=True)
    event_type = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'event_type'


class GovLocation(models.Model):
    name = models.CharField(max_length=1024)
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
        managed = False
        db_table = 'gov_location'


class Loaction(models.Model):
    location_id = models.AutoField(db_column='Location_ID', primary_key=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'loaction'


class Member(models.Model):
    memberid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    memberlevel = models.IntegerField()
    regdate = models.FloatField()
    lastlogin = models.FloatField()
    blocked = models.IntegerField()
    activated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'member'


class RelateLocation(models.Model):
    school_id = models.IntegerField(db_column='School_id', primary_key=True)  # Field name made lowercase.
    locaiton_id = models.IntegerField(db_column='Locaiton_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relate_location'
        unique_together = (('school_id', 'locaiton_id'),)


class Religion(models.Model):
    religion_id = models.AutoField(db_column='Religion_id', primary_key=True)  # Field name made lowercase.
    religion = models.CharField(db_column='Religion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'religion'


class ResourcesSubject(models.Model):
    resources_subject_id = models.AutoField(db_column='Resources_Subject_ID', primary_key=True)  # Field name made lowercase.
    resources_subject = models.CharField(db_column='Resources_Subject', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resources_subject'


class ResourcesType(models.Model):
    resources_type_id = models.AutoField(db_column='Resources_Type_ID', primary_key=True)  # Field name made lowercase.
    resources_type = models.CharField(db_column='Resources_Type', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resources_type'


class School(models.Model):
    school_id = models.AutoField(db_column='School_ID', primary_key=True)  # Field name made lowercase.
    school_name = models.CharField(db_column='School_Name', max_length=150, blank=True, null=True)  # Field name made lowercase.
    school_address = models.CharField(db_column='School_Address', max_length=500, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=11, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=11, blank=True, null=True)  # Field name made lowercase.
    supervisor_or_chairman = models.CharField(db_column='Supervisor_Or_Chairman', max_length=100, blank=True, null=True)  # Field name made lowercase.
    school_head = models.CharField(db_column='School_Head', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=200, blank=True, null=True)  # Field name made lowercase.
    school_photo = models.CharField(db_column='School_photo', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    facility = models.CharField(db_column='Facility', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    motto = models.CharField(db_column='Motto', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    mission = models.CharField(db_column='Mission', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    development_key = models.CharField(db_column='Development_Key', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    subject_by_chinese = models.CharField(db_column='Subject_By_Chinese', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    subject_by_english = models.CharField(db_column='Subject_By_English', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    location_id = models.CharField(db_column='Location_ID', max_length=11, blank=True, null=True)  # Field name made lowercase.
    funding_type_id = models.IntegerField(db_column='Funding_Type_ID')  # Field name made lowercase.
    school_net_id = models.CharField(db_column='School_Net_ID', max_length=11, blank=True, null=True)  # Field name made lowercase.
    day_type_id = models.CharField(db_column='Day_Type_ID', max_length=11, blank=True, null=True)  # Field name made lowercase.
    student_gender_id = models.CharField(db_column='Student_Gender_ID', max_length=11, blank=True, null=True)  # Field name made lowercase.
    education_type_id = models.CharField(db_column='Education_Type_ID', max_length=11, blank=True, null=True)  # Field name made lowercase.
    religion_id = models.CharField(db_column='Religion_ID', max_length=11, blank=True, null=True)  # Field name made lowercase.
    total_teacher = models.CharField(db_column='Total_Teacher', max_length=11, blank=True, null=True)  # Field name made lowercase.
    teacher_diploma = models.CharField(db_column='Teacher_Diploma', max_length=11, blank=True, null=True)  # Field name made lowercase.
    teacher_bachelor = models.CharField(db_column='Teacher_Bachelor', max_length=11, blank=True, null=True)  # Field name made lowercase.
    teacher_master_above = models.CharField(db_column='Teacher_Master_Above', max_length=11, blank=True, null=True)  # Field name made lowercase.
    teacher_04year = models.CharField(db_column='Teacher_04Year', max_length=11, blank=True, null=True)  # Field name made lowercase.
    teacher_59year = models.CharField(db_column='Teacher_59Year', max_length=11, blank=True, null=True)  # Field name made lowercase.
    teacher_10year_above = models.CharField(db_column='Teacher_10Year_Above', max_length=11, blank=True, null=True)  # Field name made lowercase.
    websitehtml = models.TextField(blank=True, null=True)
    websiteupdate = models.IntegerField()
    banding = models.CharField(db_column='Banding', max_length=30)  # Field name made lowercase.
    percentageof3322in4 = models.CharField(db_column='PercentageOf3322In4', max_length=30)  # Field name made lowercase.
    lv3chinese = models.CharField(db_column='Lv3Chinese', max_length=30)  # Field name made lowercase.
    lv3english = models.CharField(db_column='Lv3English', max_length=30)  # Field name made lowercase.
    percentagetouni = models.CharField(db_column='PercentageToUni', max_length=30)  # Field name made lowercase.
    percentageof14markin6 = models.CharField(db_column='PercentageOf14MarkIn6', max_length=30)  # Field name made lowercase.
    boyathleticrank = models.CharField(db_column='BoyAthleticRank', max_length=30)  # Field name made lowercase.
    girlathleticrank = models.CharField(db_column='GirlAthleticRank', max_length=30)  # Field name made lowercase.
    boyftballrank = models.CharField(db_column='BoyFtballRank', max_length=30)  # Field name made lowercase.
    girlftballrank = models.CharField(db_column='GirlFtballRank', max_length=30)  # Field name made lowercase.
    boyswimrank = models.CharField(db_column='BoySwimRank', max_length=30)  # Field name made lowercase.
    girlswimrank = models.CharField(db_column='GirlSwimRank', max_length=30)  # Field name made lowercase.
    boybasketrank = models.CharField(db_column='BoyBasketRank', max_length=30)  # Field name made lowercase.
    girlbasketrank = models.CharField(db_column='GirlBasketRank', max_length=30)  # Field name made lowercase.
    ntboyrank = models.CharField(db_column='NTBoyRank', max_length=30)  # Field name made lowercase.
    ntgirlrank = models.CharField(db_column='NTGirlRank', max_length=30)  # Field name made lowercase.
    musicfirst = models.CharField(db_column='MusicFirst', max_length=30)  # Field name made lowercase.
    musicsecond = models.CharField(db_column='MusicSecond', max_length=30)  # Field name made lowercase.
    musicthird = models.CharField(db_column='MusicThird', max_length=30)  # Field name made lowercase.
    speechfirst = models.CharField(db_column='SpeechFirst', max_length=30)  # Field name made lowercase.
    speechsecond = models.CharField(db_column='SpeechSecond', max_length=30)  # Field name made lowercase.
    speechthird = models.CharField(db_column='SpeechThird', max_length=30)  # Field name made lowercase.
    other_music = models.CharField(db_column='Other_Music', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'school'


class SchoolApplyNumber(models.Model):
    school_id = models.IntegerField(db_column='School_ID', primary_key=True)  # Field name made lowercase.
    apply_num = models.IntegerField(db_column='Apply_num')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'school_apply_number'


class SchoolEvent(models.Model):
    school_id = models.IntegerField(db_column='School_ID')  # Field name made lowercase.
    event_id = models.IntegerField(db_column='Event_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'school_event'


class SchoolFunding(models.Model):
    school_funding_id = models.AutoField(db_column='School_Funding_ID', primary_key=True)  # Field name made lowercase.
    school_funding = models.CharField(db_column='School_Funding', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'school_funding'


class SchoolGooglePlaceid(models.Model):
    school_id = models.IntegerField(db_column='School_ID', primary_key=True)  # Field name made lowercase.
    google_place_id = models.CharField(db_column='Google_Place_ID', max_length=32)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    address = models.TextField(db_column='Address')  # Field name made lowercase.
    geometry_lat = models.FloatField(db_column='Geometry_Lat')  # Field name made lowercase.
    geometry_lng = models.FloatField(db_column='Geometry_Lng')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'school_google_placeid'


class SchoolNet(models.Model):
    school_net_id = models.IntegerField(db_column='School_Net_ID', primary_key=True)  # Field name made lowercase.
    school_net = models.CharField(db_column='School_Net', max_length=1200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'school_net'


class SchoolPicking(models.Model):
    school_picking_id = models.AutoField(db_column='School_Picking_ID', primary_key=True)  # Field name made lowercase.
    school_picking_title = models.CharField(db_column='School_Picking_title', max_length=150)  # Field name made lowercase.
    education_type_id = models.IntegerField(db_column='Education_Type_ID')  # Field name made lowercase.
    detail = models.TextField(db_column='Detail', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'school_picking'


class SchoolRelateLocation(models.Model):
    school_id = models.IntegerField(db_column='School_ID', primary_key=True)  # Field name made lowercase.
    location_id = models.IntegerField(db_column='Location_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'school_relate_location'
        unique_together = (('school_id', 'location_id'),)


class StudentGender(models.Model):
    student_gender_id = models.AutoField(db_column='Student_Gender_ID', primary_key=True)  # Field name made lowercase.
    student_gender = models.CharField(db_column='Student_Gender', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student_gender'


class StudyResources(models.Model):
    study_resources_id = models.AutoField(db_column='Study_Resources_ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=150)  # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=50)  # Field name made lowercase.
    link = models.CharField(db_column='Link', max_length=150)  # Field name made lowercase.
    resources_subject_id = models.IntegerField(db_column='Resources_Subject_ID')  # Field name made lowercase.
    resources_type_id = models.IntegerField(db_column='Resources_Type_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'study_resources'
