#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "longyucen"
# Date: 2018/7/7
from svn import models
import time


def vesrion_update(pt_id, model_id, model_path, v1, v2, v3, v4, version_d, tag_message):
    version_reslut = models.TbModuleVersion.objects.filter(pre_plat_id_id=pt_id).filter(pre_module_id=model_id).first()
    update_time = time.strftime('%YY%m%d ')
    print(version_reslut)
    # 判断该模块有未初始化版本信
    if version_reslut:
        # 增加最大版本号
        a = models.TbModuleVersion.objects.filter(pre_module_id_id=model_id).filter(
            pre_plat_id_id=pt_id).first()
        # 要升级的版本号
        b = 'a.v' + str(version_d)
        c = 'v' + str(version_d)
        version_id = eval(b)
        version_id = version_id + 1
        version = ''
        if c == 'v1':
            version = str(version_id) + '.' + str(a.v2) + '.' + str(a.v3) + '.' + str(a.v4)
            model_path = model_path + '_' + version
        elif c == 'v2':
            version = str(a.v1) + '.' + str(version_id) + '.' + str(a.v3) + '.' + str(a.v4)
            model_path = model_path + '_' + version
        elif c == 'v3':
            version = str(a.v1) + '.' + str(a.v2) + '.' + str(version_id) + '.' + str(a.v4)
            model_path = model_path + '_' + version
        elif c == 'v4':
            version = str(a.v1) + '.' + str(a.v2) + '.' + str(a.v3) + '.' + str(version_id)
            model_path = model_path + '_' + version
        print('地址：', model_path)
        print('version', version)
        print('version_id:', version_id)
        line = "models.TbModuleVersion.objects.filter(pre_module_id_id=model_id).filter(pre_plat_id_id=pt_id).\
                update(%s=%s)" % (c, version_id)
        result = eval(line)
        models.TbModuleVersion.objects.filter(pre_module_id_id=model_id).filter(pre_plat_id_id=pt_id).\
            update(pre_tag_path=model_path)
        models.TbRecord.objects.create(bef_plat_id_id=pt_id, bef_module_id_id=model_id, bef_tag_path=model_path, \
                                       bef_version=version, cause=tag_message)
        print('返回结果:', result)
    # 初始化版本信息
    else:
        version = str(v1) + '.' + str(v2) + '.' + str(v3) + '.' + str(v4)
        model_path = model_path + '_' + version
        models.TbModuleVersion.objects.create(pre_plat_id_id=pt_id, pre_module_id_id=model_id, \
                                              pre_tag_path=model_path, v1=v1, v2=v2, v3=v3, v4=v4)
        models.TbRecord.objects.create(bef_plat_id_id=pt_id, bef_module_id_id=model_id, bef_tag_path=model_path, \
                                       bef_version=version, cause=tag_message)