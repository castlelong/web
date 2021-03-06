# Generated by Django 2.0.6 on 2018-07-06 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbModu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modu_name', models.CharField(db_column='modu_name', max_length=40, unique=True, verbose_name='模块名')),
                ('modu_add', models.CharField(db_column='modu_add', max_length=100, verbose_name='模块地址')),
            ],
            options={
                'verbose_name': '模块列表',
                'verbose_name_plural': '模块列表',
            },
        ),
        migrations.CreateModel(
            name='TbModuleVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v1', models.IntegerField(verbose_name='版本号')),
                ('v2', models.IntegerField(verbose_name='版本号')),
                ('v3', models.IntegerField(verbose_name='版本号')),
                ('v4', models.IntegerField(verbose_name='版本号')),
                ('last_update_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('pre_tag_path', models.CharField(max_length=200, verbose_name='当前tag路径')),
                ('cause', models.CharField(max_length=400, verbose_name='更新原因')),
                ('pre_module_id', models.ForeignKey(db_column='pre_module_id', on_delete=django.db.models.deletion.CASCADE, to='svn.TbModu')),
            ],
            options={
                'verbose_name': '模块版本表',
                'verbose_name_plural': '模块版本表',
            },
        ),
        migrations.CreateModel(
            name='TbPlat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plat_jc', models.CharField(db_column='plat_jc', max_length=10, unique=True, verbose_name='平台简称')),
                ('plat_name', models.CharField(db_column='plat_name', max_length=40, unique=True, verbose_name='平台名')),
            ],
            options={
                'verbose_name': '平台列表',
                'verbose_name_plural': '平台列表',
            },
        ),
        migrations.CreateModel(
            name='TbRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bef_version', models.CharField(max_length=10, verbose_name='历史版本')),
                ('update_date', models.DateTimeField(verbose_name='更新时间')),
                ('cause', models.CharField(max_length=400, verbose_name='更新原因')),
                ('bef_tag_path', models.CharField(max_length=200, verbose_name='对应tag路径')),
                ('bef_module_id', models.ForeignKey(db_column='bef_module_id', on_delete=django.db.models.deletion.CASCADE, to='svn.TbModu')),
                ('bef_plat_id', models.ForeignKey(db_column='bef_plat_id', on_delete=django.db.models.deletion.CASCADE, to='svn.TbPlat')),
            ],
            options={
                'verbose_name': '更新记录表',
                'verbose_name_plural': '更新记录表',
            },
        ),
        migrations.AddField(
            model_name='tbmoduleversion',
            name='pre_plat_id',
            field=models.ForeignKey(db_column='pre_plat_id', on_delete=django.db.models.deletion.CASCADE, to='svn.TbPlat'),
        ),
        migrations.AlterIndexTogether(
            name='tbrecord',
            index_together={('bef_plat_id', 'bef_module_id')},
        ),
        migrations.AlterUniqueTogether(
            name='tbmoduleversion',
            unique_together={('pre_plat_id', 'pre_module_id')},
        ),
    ]
