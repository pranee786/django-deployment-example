# -*- coding: utf-8 -*-
from django.urls import path
from basicapp import views

#TEMPLATE TAGGING
app_name = 'basicapp'

urlpatterns = [
        path('',views.index,name="index"),
        path('other/',views.other,name="other"),
        path('relative/',views.relative,name="relative"),
    ]
