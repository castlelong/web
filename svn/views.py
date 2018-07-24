from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import datetime
import time
from svn import update
# Create your views here.
from django.views import View
from svn import models
from svn import svncontorl
# plat_dict ={
#     'xft':'信付通平台(线下平台)',
#     'syxl':'商银信联平台(线上平台)'
# }


class Platform(View):

    def dispatch(self, request, *args, **kwargs):
        reslut = super(Platform, self).dispatch(request, *args, **kwargs)
        return reslut

    def get(self, request):
        plat_dict = {}
        result = models.TbPlat.objects.all()
        for row in result:
            plat_dict.update({row.plat_jc: row.plat_name})
        return render(request, 'svn/platform.html', {'plat_dict': plat_dict})

    def post(self, request):
        jc = request.POST.get('plat_jc')
        name = request.POST.get('plat_name')
        if request.POST.get('fanhui'):
            return redirect('/index/')
        elif jc == '' or name == '':
            error_message = "未输入相关参数，请认真填写！"
            plat_dict = {}
            result = models.TbPlat.objects.all()
            for row in result:
                plat_dict.update({row.plat_jc: row.plat_name})
            return render(request, 'svn/platform.html', {"error_message": error_message, 'plat_dict': plat_dict})

        else:
            models.TbPlat.objects.create(plat_jc=jc, plat_name=name)
            # return render(request, 'svn/platform.html')
            return redirect('/platform/')


class Model(View):

    def dispatch(self, request, *args, **kwargs):

        reslut = super(Model, self).dispatch(request, *args, **kwargs)
        return reslut

    def get(self, request):
        result = models.TbModu.objects.all()
        return render(request, 'svn/model.html', {'mod_result': result})

    def post(self, request):
        name = request.POST.get('modle_name')
        add = request.POST.get('svn_add')
        if name == '' or add == '':
            result = models.TbModu.objects.all()
            error_message = "未输入相关参数，请认真填写！"
            return render(request, 'svn/model.html', {"error_message": error_message, 'mod_result': result})
        else:
            name = request.POST.get('modle_name')
            add = request.POST.get('svn_add')
            models.TbModu.objects.create(modu_name=name, modu_add=add)
            return redirect('/model/')




class Tag(View):

    def dispatch(self, request, *args, **kwargs):

        reslut = super(Tag, self).dispatch(request, *args, **kwargs)
        return reslut

    def get(self, request):
        model_result = models.TbModu.objects.all()
        pt_result = models.TbPlat.objects.all()
        tag_result = models.Huanjin.objects.all()
        return render(request, 'svn/tag.html', {'model_list': model_result, 'pt_list': pt_result, 'tag_list': tag_result})

    def post(self, request):
        pt_id = request.POST.get('ptmc')
        model_id = request.POST.get('mkmc')
        tag_id = request.POST.get('mkhj')
        tag_result = models.Huanjin.objects.filter(id=tag_id).first()
        tag_name = tag_result.h_name
        tag_bj = tag_result.tag_bj
        tag_message = request.POST.get('message')
        tag_date = time.strftime('%Y%m%d', time.localtime())
        v1 = 1
        v2 = 0
        v3 = 0
        v4 = 0
        # add = "http://10.200.201.120/svn/luban/tags"  # SVN版本的tag分支存放路径
        add = "http://10.200.201.120/svn/cx/%s" % tag_bj
        print('add:', add)
        pass
        # 获取模块SVN主版本路径
        model_result = models.TbModu.objects.filter(id=model_id).first()
        svn_add = model_result.modu_add  # 模块主干地址
        print(svn_add)
        # 获取模块名称
        model_name = model_result.modu_name
        # 获取SVN版本号
        model_version = svncontorl.version(svn_add)
        # 拼接一个带模块版本号的地址，如：http://10.200.201.120/svn/cx/tags/"模块名"/"主干版本号"_更新日期
        model_path = add + '/' + model_name + '/' + model_version + '_' + tag_date
        # 拼接一个模块的tag分支存放路径地址，如：http://10.200.201.120/svn/cx/tags/"模块名"/
        tag_model_path = add + '/' + model_name + '/'
        # 根据按钮完成版本的升级
        if request.POST.get('v1'):
            version_d = 1
            # 返回完整带版本信息的SVN路径
            version_model_path = update.vesrion_update(pt_id, model_id, model_path, v1, v2, v3, v4, version_d, tag_message)
            # print('end_model_path:', end_model_path)
            svncontorl.set_parm(svn_add, tag_model_path, tag_message, version_model_path)
        elif request.POST.get('v2'):
            version_d = 2
            version_model_path = update.vesrion_update(pt_id, model_id, model_path, v1, v2, v3, v4, version_d, tag_message)
            svncontorl.set_parm(svn_add, tag_model_path, tag_message, version_model_path)
        elif request.POST.get('v3'):
            version_d = 3
            version_model_path = update.vesrion_update(pt_id, model_id, model_path, v1, v2, v3, v4, version_d, tag_message)
            svncontorl.set_parm(svn_add, tag_model_path, tag_message, version_model_path)
        elif request.POST.get('v4'):
            version_d = 4
            version_model_path = update.vesrion_update(pt_id, model_id, model_path, v1, v2, v3, v4, version_d, tag_message)
            svncontorl.set_parm(svn_add, tag_model_path, tag_message, version_model_path)
        elif request.POST.get('fanhui'):
            return redirect('/index/')
        return redirect('/tag/')


class Search(View):
    def dispatch(self, request, *args, **kwargs):
        reslut = super(Search, self).dispatch(request, *args, **kwargs)
        return reslut

    def get(self, request):
        plat_result = models.TbPlat.objects.all()
        model_result = models.TbModu.objects.all()
        return render(request, 'svn/search.html', {'plat_list': plat_result, 'model_list': model_result})

    def post(self, request):
        if request.POST.get('search'):
            plat_result = models.TbPlat.objects.all()
            model_result = models.TbModu.objects.all()
            pt_id = request.POST.get('ptmc')
            mk_id = request.POST.get('mkmc')
            if pt_id or mk_id:
                if pt_id and mk_id:
                    result = models.TbRecord.objects.filter(bef_plat_id_id=pt_id).filter(bef_module_id_id=mk_id)
                elif pt_id:
                    result = models.TbRecord.objects.filter(bef_plat_id_id=pt_id)
                elif mk_id:
                    result = models.TbRecord.objects.filter(bef_module_id_id=mk_id)
            else:
                result = models.TbRecord.objects.all()
                for row in result:
                    print(type(row.update_date), row.update_date)
            return render(request, 'svn/search.html', {'plat_list': plat_result, 'model_list': model_result, \
                                                       'model_recoder': result})


class Login(View):
    def dispatch(self, request, *args, **kwargs):
        reslut = super(Login, self).dispatch(request, *args, **kwargs)
        return reslut

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        if request.POST.get('tijiao'):
            user = request.POST.get('user')
            pwd = request.POST.get('password')
            print(user, pwd)
            u = models.Userinfo.objects.filter(user=user).filter(password=pwd).first()
            user_name = u.user
            passd = u.password
            if user == ' ' and pwd == ' ':
                error_message = "未输入相关参数，请认真填写！"
                return render(request, 'login.html', {'error_message': error_message})
            elif user == user_name and pwd == passd:
                return redirect('/index/')
            else:
                error_message = "用户名或密码错误"
                return render(request, 'login.html', {'error_message': error_message})


def index(request):
    return render(request, 'index.html')