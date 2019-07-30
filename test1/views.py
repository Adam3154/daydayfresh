from django.shortcuts import render
from django.http import *
# Create your views here.
def index(request):
    # temp=loader.get_template('booktest/index.html')
    # return HttpResponse(temp.render())
    #
    return render(request,'test1/index.html')
    #return HttpResponse('hello world')

def register(request):
    return  render(request,'test1/register.html')