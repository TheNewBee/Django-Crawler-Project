"""hkeasyschool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import view,maindb,membersystem,choiceguideform,schoolmap

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', view.index),
    url(r'^index$', view.index),
    url(r'^contact$', view.contact),
    url(r'^school-news$', view.school_news),
    url(r'^school-ranking$', view.school_ranking),
    url(r'^school-info$', view.school_info),
    url(r'^choice-guide$', view.choice_guide),
    url(r'^form$', choiceguideform.formsubmit),

    url(r'^school-map$', schoolmap.schoolmap),
    url(r'^functions/schoolmap$', schoolmap.functions_schoolmap),
    url(r'^functions/schoolmap.xml$', schoolmap.functions_schoolmapxml),
    url(r'^functions/getSchoolDetails$', schoolmap.functions_getSchoolDetails),

    url(r'^login$', membersystem.login),
    url(r'^register$', membersystem.register),
    #url(r'^encrypttest$', membersystem.test),
]
