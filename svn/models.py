from django.db import models

# Create your models here.
from django.db import models


class TbPlat(models.Model):
    plat_jc = models.CharField("平台简称", max_length=10, unique=True, db_column="plat_jc")
    plat_name = models.CharField("平台名", max_length=40, unique=True, db_column="plat_name")

    def __str__(self):
        return self.plat_name   #在后台管理页中返回指定字段内容

    class Meta:
        verbose_name = '平台列表'
        verbose_name_plural = verbose_name


class TbModu(models.Model):
    modu_name = models.CharField("模块名", max_length=40, unique=True, db_column="modu_name")
    modu_add = models.CharField("模块地址", max_length=100, db_column="modu_add")

    def __str__(self):
        return self.modu_name   #在后台管理页中返回指定字段内容

    class Meta:
        verbose_name = '模块列表'
        verbose_name_plural = verbose_name


class TbModuleVersion(models.Model):
    pre_plat_id = models.ForeignKey(TbPlat, on_delete=models.CASCADE, db_column="pre_plat_id")
    pre_module_id = models.ForeignKey(TbModu, on_delete=models.CASCADE, db_column="pre_module_id")
    v1 = models.IntegerField("版本号")
    v2 = models.IntegerField("版本号")
    v3 = models.IntegerField("版本号")
    v4 = models.IntegerField("版本号")
    last_update_time = models.DateTimeField("最后更新时间", auto_now=True)
    pre_tag_path = models.CharField("当前tag路径", max_length=200)

    class Meta:
        unique_together = [('pre_plat_id', 'pre_module_id',)]
        verbose_name = '模块版本表'
        verbose_name_plural = verbose_name


class TbRecord(models.Model):
    bef_plat_id = models.ForeignKey(TbPlat, on_delete=models.CASCADE, db_column="bef_plat_id")
    bef_module_id = models.ForeignKey(TbModu, on_delete=models.CASCADE, db_column="bef_module_id")
    bef_version = models.CharField("历史版本", max_length=10)
    update_date = models.DateTimeField("更新时间")
    cause = models.CharField("更新原因", max_length=400)
    bef_tag_path = models.CharField("对应tag路径", max_length=200)

    class Meta:
        index_together = [('bef_plat_id', 'bef_module_id'), ]
        verbose_name = '更新记录表'
        verbose_name_plural = verbose_name

