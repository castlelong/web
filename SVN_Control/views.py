from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.



# def index(request):
#     return HttpResponse("Hello, world. You're at the SVN index.")


# def platform(request):
# #     if request.method == 'POST':
# #         jc = request.POST.get('plat_jc')
# #         name = request.POST.get('plat_name')
# #         if jc == '' or name == '':
# #             print(123)
# #             error_message = "未输入相关参数，请认真填写！"
# #             # return redirect("platform", {"error_message": error_message})
# #             return render(request, "svn/platform.html", {"error_message": error_message})
# #
# #     # else:
# #     #     return redirect("/platform")
# #     return render(request, "svn/platform.html")

from django.views import View
plat_dict ={
    'xft':'信付通平台(线下平台)',
    'syxl':'商银信联平台(线上平台)'
}


class Platform(View):

    def dispatch(self, request, *args, **kwargs):

        reslut = super(Platform, self).dispatch(request, *args, **kwargs)
        return reslut

    def get(self, request):
        return render(request, 'svn/platform.html', {'plat_dict': plat_dict})

    def post(self, request):
        jc = request.POST.get('plat_jc')
        name = request.POST.get('plat_name')
        if jc == '' or name == '':
            error_message = "未输入相关参数，请认真填写！"
            return render(request, 'svn/platform.html', {"error_message": error_message})
        else:

            return render(request, 'svn/platform.html')


def index(request):
    return render(request, 'index.html')