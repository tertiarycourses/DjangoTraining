from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<p>home view</p>')

def post_detail(request, id):
    return HttpResponse('<p>Post view with the id {}</p>'.format(id))
