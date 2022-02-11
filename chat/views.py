from django.shortcuts import redirect, render
from chat.forms import chatform
from chat.models import chatmodel
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/a/login/')
def chatview(request):
    form=chatform()
    res=chatmodel.objects.all()
    if request.method=='POST':
        form=chatform(request.POST,request.FILES)
        if form.is_valid():
            chatmodel.objects.create(cid_id=request.user.id,
                                     msg=form.cleaned_data['msg'],
                                     cimg=form.cleaned_data['cimg'],
                                     cfile=form.cleaned_data['cfile'])
            return render(request,'chat.html',{'form':form,'res':res})
    return render(request,'chat.html',{'form':form,'res':res})
