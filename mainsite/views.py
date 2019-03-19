from django.shortcuts import render
from django import forms
from django.template.loader import get_template
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from mainsite.models import user
from django.template import RequestContext


# Create your views here.
class UserForm(forms.Form):
    userid = forms.CharField(label='账号')
    passwd = forms.CharField(label='密码',widget=forms.PasswordInput)

def home(request):
    if 'userid' in request.session:
        userid = request.session['userid']
        return render(request,'home.html',{'userid':userid})
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        rg = UserForm(request.POST)
        if rg.is_valid():
            userid = rg.cleaned_data['userid']
            passwd = rg.cleaned_data['passwd']
            u = user()
            u.user_id = userid
            u.user_passwd = passwd
            u.save()
            return HttpResponseRedirect('/login/')
    else:
        rg = UserForm()
    return render(request,'register.html',{'rg':rg})

def login(req):
    if req.method == 'POST':
        log = UserForm(req.POST)
        if log.is_valid():
            userid = log.cleaned_data['userid']
            passwd = log.cleaned_data['passwd']
            user1 = user.objects.filter(user_id__exact=userid, user_passwd__exact=passwd)
            if user1:
                req.session['userid'] = userid
                return render(req,'home.html',{'userid':userid})
                # return HttpResponseRedirect('/home/')
            else:
                return HttpResponseRedirect('/login/')
    else:
        log = UserForm()
    return render(req,'login.html',{'log':log})
#注销操作
def logout(req):
    del req.session['userid']
    return render(req,'home.html')
