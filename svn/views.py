from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import datetime
import time
from svn import update
# Create your views here.
from django.views import View
from svn import models
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
        return render(request, 'svn/tag.html', {'model_list': model_result, 'pt_list': pt_result})

    def post(self, request):
        pt_id = request.POST.get('ptmc')
        model_id = request.POST.get('mkmc')
        tag_message = request.POST.get('message')
        tag_date = time.strftime('%Y%m%d', time.localtime())
        v1 = 1
        v2 = 0
        v3 = 0
        v4 = 0
        model_result = models.TbModu.objects.filter(id=model_id).first()
        svn_add = "http://10.200.200.21:18443"
        model_name = model_result.modu_name
        model_version = '8043'
        model_path = svn_add + '/' + model_name + '/' + model_version + '_' + tag_date
        print(model_path)
        pass
        if request.POST.get('v1'):
            version_d = 1
            update.vesrion_update(pt_id, model_id, model_path, v1, v2, v3, v4, version_d, tag_message)
        elif request.POST.get('v2'):
            version_d = 2
            update.vesrion_update(pt_id, model_id, model_path, v1, v2, v3, v4, version_d, tag_message)
        elif request.POST.get('v3'):
            version_d = 3
            update.vesrion_update(pt_id, model_id, model_path, v1, v2, v3, v4, version_d, tag_message)
        elif request.POST.get('v4'):
            version_d = 4
            update.vesrion_update(pt_id, model_id, model_path, v1, v2, v3, v4, version_d, tag_message)
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
                    print(type(row.update_date),row.update_date)
            return render(request, 'svn/search.html', {'plat_list': plat_result, 'model_list': model_result, \
                                                       'model_recoder': result})


def index(request):
    return render(request, 'index.html')