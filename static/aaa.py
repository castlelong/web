#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "longyucen"
# Date: 2018/7/7

c = 'v1'
version = '10'

v_list = ['v1', 'v2', 'v3', 'v4']
# v_list[v_list.index(c)] = version
a = 0
for row in v_list:
    print(v_list.index(row))
    if v_list.index(row) == v_list.index(c):
        print('aaaaaa')
    a += 1
    print(a)
print(v_list)
