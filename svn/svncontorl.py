#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "longyucen"
# Date: 2018/7/8
# coding=utf-8
from svn import models
import os
# import time
import sys
import chardet


def set_parm(svn_add, tag_model_path, tag_message, version_model_path):
    # print(svn_add, end_model_path)
    setting = {
        'svn': '/usr/bin/svn',  # svn的程序所在路径
        'url': svn_add,  # 模块SVN主版本地址
        'user': 'svnadmin',  # 用户名
        'pwd': 'svnadmin',  # 密码
        'tag_path': tag_model_path,  # 模块tag地址
        'message': tag_message,  # 提交信息
        'version_model_path': version_model_path# 最终带版本的SVN分支路径

        # 'interval':15 #更新时间
    }
    print('set:', setting)
    tag(setting)


def tag(setting):
    print('tag:', setting)
    dir_info = "svn info " + setting['tag_path'] + " " + "--username svnadmin --password svnadmin"
    dir_result = os.system(dir_info)  # 得到命令运行结果值，0为成功，1为失败
    print('dir_result:', dir_result)
    print('message:', chardet.detect(setting['message'].encode(encoding='utf-8')))
    # message = setting['message']
    # pass
    if dir_result != 0:
        mk_path = 'svn mkdir -m' + ' ' + 'mkdir' + ' ' + setting['tag_path'] \
                  + ' ' + '--username' + ' ' + setting['user'] + ' ' + "--password" + ' ' + setting['pwd']
        print('mk_path:', mk_path)
        os.popen(mk_path)
    tag_cmd = 'svn cp' + ' ' + '-m' + ' ' + 'tag' + ' ' + setting['url'] + \
              ' ' + setting['version_model_path'] + ' ' + '--username' + ' ' + \
              setting['user'] + ' ' + '--password' + ' ' + setting['pwd']
    # tag_cmd = ('svn cp -m' + ' ' + '%s' + ' ' + setting['url'] + \
    #           ' ' + setting['version_model_path'] + ' ' + '--username' + ' ' + \
    #           setting['user'] + ' ' + '--password' + ' ' + setting['pwd']) % setting['message']
    print(tag_cmd, type(tag_cmd))
    os.popen(tag_cmd)
    # print(sys.getdefaultencoding())
    print('tag_cmd:', tag_cmd)


def version(svn_add):
    """
    获取svn版本号
    :param svn_add:
    :return: 主版本的SVN版本号
    """
    svn_cmd = "svn info " + svn_add + " " + "--username svnadmin --password svnadmin"
    # print(svn_cmd)
    svn_info = os.popen(svn_cmd).read()
    # print(svn_info)
    svn_info_list = svn_info.strip(',').split('\n')
    version_list = svn_info_list[5]
    # print(svn_info_list, version_list)
    reversion = version_list[10:]
    print(reversion)
    return reversion
