from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.core.files.storage import FileSystemStorage
def imageprocess(request):
    IF=ImageForm()
    d={'IF':IF}
    if request.method=='POST' and request.FILES:
        FD=ImageForm(request.POST,request.FILES)
        if FD.is_valid():
            img=FD.cleaned_data['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
            image_url=fs.url(file)
            d1={'image_url':image_url}
            return render(request,'savedimage.html',d1)

    return render(request,'ig.html',d)