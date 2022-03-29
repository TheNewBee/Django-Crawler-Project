# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-15 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DayType',
            fields=[
                ('day_type_id', models.AutoField(db_column='Day_Type_ID', primary_key=True, serialize=False)),
                ('day_type', models.CharField(db_column='Day_Type', max_length=10)),
            ],
            options={
                'db_table': 'day_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EducationType',
            fields=[
                ('education_type_id', models.AutoField(db_column='Education_Type_ID', primary_key=True, serialize=False)),
                ('education_type', models.CharField(db_column='Education_Type', max_length=50)),
            ],
            options={
                'db_table': 'education_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EventInfo',
            fields=[
                ('event_id', models.AutoField(db_column='Event_ID', primary_key=True, serialize=False)),
                ('start_date', models.DateField(blank=True, db_column='Start_Date', null=True)),
                ('end_date', models.DateField(blank=True, db_column='End_Date', null=True)),
                ('title', models.CharField(blank=True, db_column='Title', max_length=150, null=True)),
                ('remark', models.CharField(blank=True, db_column='Remark', max_length=3000, null=True)),
                ('event_type', models.IntegerField(blank=True, db_column='Event_Type', null=True)),
                ('link', models.CharField(blank=True, db_column='Link', max_length=400, null=True)),
            ],
            options={
                'db_table': 'event_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('event_type_id', models.IntegerField(primary_key=True, serialize=False)),
                ('event_type', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'event_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GovLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
            options={
                'db_table': 'gov_location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Loaction',
            fields=[
                ('location_id', models.AutoField(db_column='Location_ID', primary_key=True, serialize=False)),
                ('location', models.CharField(db_column='Location', max_length=50)),
            ],
            options={
                'db_table': 'loaction',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RelateLocation',
            fields=[
                ('school_id', models.IntegerField(db_column='School_id', primary_key=True, serialize=False)),
                ('locaiton_id', models.IntegerField(db_column='Locaiton_id')),
            ],
            options={
                'db_table': 'relate_location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('religion_id', models.AutoField(db_column='Religion_id', primary_key=True, serialize=False)),
                ('religion', models.CharField(db_column='Religion', max_length=50)),
            ],
            options={
                'db_table': 'religion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ResourcesSubject',
            fields=[
                ('resources_subject_id', models.AutoField(db_column='Resources_Subject_ID', primary_key=True, serialize=False)),
                ('resources_subject', models.CharField(db_column='Resources_Subject', max_length=60)),
            ],
            options={
                'db_table': 'resources_subject',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ResourcesType',
            fields=[
                ('resources_type_id', models.AutoField(db_column='Resources_Type_ID', primary_key=True, serialize=False)),
                ('resources_type', models.CharField(db_column='Resources_Type', max_length=60)),
            ],
            options={
                'db_table': 'resources_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_id', models.AutoField(db_column='School_ID', primary_key=True, serialize=False)),
                ('school_name', models.CharField(blank=True, db_column='School_Name', max_length=150, null=True)),
                ('school_address', models.CharField(blank=True, db_column='School_Address', max_length=500, null=True)),
                ('telephone', models.CharField(blank=True, db_column='Telephone', max_length=11, null=True)),
                ('fax', models.CharField(blank=True, db_column='Fax', max_length=11, null=True)),
                ('supervisor_or_chairman', models.CharField(blank=True, db_column='Supervisor_Or_Chairman', max_length=100, null=True)),
                ('school_head', models.CharField(blank=True, db_column='School_Head', max_length=100, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=100, null=True)),
                ('website', models.CharField(blank=True, db_column='Website', max_length=200, null=True)),
                ('school_photo', models.CharField(blank=True, db_column='School_photo', max_length=1000, null=True)),
                ('facility', models.CharField(blank=True, db_column='Facility', max_length=1000, null=True)),
                ('motto', models.CharField(blank=True, db_column='Motto', max_length=1000, null=True)),
                ('mission', models.CharField(blank=True, db_column='Mission', max_length=1000, null=True)),
                ('development_key', models.CharField(blank=True, db_column='Development_Key', max_length=1000, null=True)),
                ('subject_by_chinese', models.CharField(blank=True, db_column='Subject_By_Chinese', max_length=1000, null=True)),
                ('subject_by_english', models.CharField(blank=True, db_column='Subject_By_English', max_length=1000, null=True)),
                ('location_id', models.CharField(blank=True, db_column='Location_ID', max_length=11, null=True)),
                ('school_net_id', models.CharField(blank=True, db_column='School_Net_ID', max_length=11, null=True)),
                ('day_type_id', models.CharField(blank=True, db_column='Day_Type_ID', max_length=11, null=True)),
                ('student_gender_id', models.CharField(blank=True, db_column='Student_Gender_ID', max_length=11, null=True)),
                ('education_type_id', models.CharField(blank=True, db_column='Education_Type_ID', max_length=11, null=True)),
                ('religion_id', models.CharField(blank=True, db_column='Religion_ID', max_length=11, null=True)),
                ('total_teacher', models.CharField(blank=True, db_column='Total_Teacher', max_length=11, null=True)),
                ('teacher_diploma', models.CharField(blank=True, db_column='Teacher_Diploma', max_length=11, null=True)),
                ('teacher_bachelor', models.CharField(blank=True, db_column='Teacher_Bachelor', max_length=11, null=True)),
                ('teacher_master_above', models.CharField(blank=True, db_column='Teacher_Master_Above', max_length=11, null=True)),
                ('teacher_04year', models.CharField(blank=True, db_column='Teacher_04Year', max_length=11, null=True)),
                ('teacher_59year', models.CharField(blank=True, db_column='Teacher_59Year', max_length=11, null=True)),
                ('teacher_10year_above', models.CharField(blank=True, db_column='Teacher_10Year_Above', max_length=11, null=True)),
                ('websitehtml', models.TextField(blank=True, null=True)),
                ('websiteupdate', models.IntegerField()),
            ],
            options={
                'db_table': 'school',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_id', models.IntegerField(db_column='School_ID')),
                ('event_id', models.IntegerField(db_column='Event_ID')),
            ],
            options={
                'db_table': 'school_event',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolFunding',
            fields=[
                ('school_funding_id', models.AutoField(db_column='School_Funding_ID', primary_key=True, serialize=False)),
                ('school_funding', models.CharField(db_column='School_Funding', max_length=100)),
            ],
            options={
                'db_table': 'school_funding',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolGooglePlaceid',
            fields=[
                ('school_id', models.IntegerField(db_column='School_ID', primary_key=True, serialize=False)),
                ('google_place_id', models.CharField(db_column='Google_Place_ID', max_length=32)),
                ('name', models.CharField(db_column='Name', max_length=64)),
                ('address', models.TextField(db_column='Address')),
                ('geometry_lat', models.FloatField(db_column='Geometry_Lat')),
                ('geometry_lng', models.FloatField(db_column='Geometry_Lng')),
            ],
            options={
                'db_table': 'school_google_placeid',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolNet',
            fields=[
                ('school_net_id', models.IntegerField(db_column='School_Net_ID', primary_key=True, serialize=False)),
                ('school_net', models.CharField(db_column='School_Net', max_length=1200)),
            ],
            options={
                'db_table': 'school_net',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolPicking',
            fields=[
                ('school_picking_id', models.AutoField(db_column='School_Picking_ID', primary_key=True, serialize=False)),
                ('school_picking_title', models.CharField(db_column='School_Picking_title', max_length=150)),
                ('education_type_id', models.IntegerField(db_column='Education_Type_ID')),
                ('detail', models.TextField(blank=True, db_column='Detail', null=True)),
            ],
            options={
                'db_table': 'school_picking',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolRelateLocation',
            fields=[
                ('school_id', models.IntegerField(db_column='School_ID', primary_key=True, serialize=False)),
                ('location_id', models.IntegerField(db_column='Location_ID')),
            ],
            options={
                'db_table': 'school_relate_location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StudentGender',
            fields=[
                ('student_gender_id', models.AutoField(db_column='Student_Gender_ID', primary_key=True, serialize=False)),
                ('student_gender', models.CharField(db_column='Student_Gender', max_length=10)),
            ],
            options={
                'db_table': 'student_gender',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StudyResources',
            fields=[
                ('study_resources_id', models.AutoField(db_column='Study_Resources_ID', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='Title', max_length=150)),
                ('author', models.CharField(db_column='Author', max_length=50)),
                ('link', models.CharField(db_column='Link', max_length=150)),
                ('resources_subject_id', models.IntegerField(db_column='Resources_Subject_ID')),
                ('resources_type_id', models.IntegerField(db_column='Resources_Type_ID')),
            ],
            options={
                'db_table': 'study_resources',
                'managed': False,
            },
        ),
    ]
