#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "longyucen"
# Date: 2018/7/8
# coding=utf-8
from svn import models
import os
import time
# import sys


def set_parm(svn_add, end_model_path, tag_message):
    print(svn_add, end_model_path)
    setting = {
        'svn': '/usr/bin/svn',  # svn的程序所在路径
        'url': svn_add,  # svn地址
        'user': 'svnadmin',  # 用户名
        'pwd': 'svnadmin',  # 密码
        'dist': end_model_path,  # 目标地址
        'message': tag_message,
        'model_path': svn_add
        # 'interval':15 #更新时间
    }
    print('set:', setting)
    tag(setting)


def tag(setting):
    print('tag:', setting)
    mk_path = 'svn mkdir -m mkdir' + ' ' + setting['model_path'] + '/tag' \
              + " " + "--username" + " " + setting['user'] + " " + "--password" + " " + setting['pwd']
    print(mk_path)
    os.popen(mk_path)
    tag_cmd = "svn cp " + " -m " + setting['message'] + " " + setting['url'] + " " + setting['dist'] + " "\
              "--username" + " " + setting['user'] + " " + "--password" + " " + setting['pwd']
    os.popen(tag_cmd)
    print('tag_cmd:', tag_cmd)
    # os.popen("svn cp " + " -m " + setting['message'] + " " + setting['url'] + " " + setting['dist'])

# def chckout(setting):
#     setting()
#     cmd = 'svn checkout %(url)s %(dist)s --username %(user)s --password %(pwd)s' % setting
#     print("execute %s" % cmd)
#     #print os.popen(cmd).read()
#     return os.system(cmd)


def version(svn_add):
    """
    获取svn版本号
    :param svn_add:
    :return:
    """
    svn_cmd = "svn info " + svn_add + " " + "--username svnadmin --password svnadmin"
    # print(svn_cmd)
    svn_info = os.popen(svn_cmd).read()
    # print(svn_info)
    svn_info_list = svn_info.strip(',').split('\n')
    version_list = svn_info_list[5]
    # print(svn_info_list, version_list)
    reversion = version_list[10:]
    # print(reversion)
    return reversion
