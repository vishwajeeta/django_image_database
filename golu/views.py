from django.shortcuts import render
from .models import images
# Create your views here.
def home(request):
    data=images.objects.all()
    return render(request,'index.html',{'data':data})