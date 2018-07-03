#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "longyucen"
# Date: 2018/6/20

from django.urls import path


app_name = 'SVN_Control'


urlpatterns = [
    path('', views.index, name='index'),
]
