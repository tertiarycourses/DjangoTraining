from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Post


def home(request):
	posts = Post.objects.all()
	return render(request,'home.html',{'posts':posts})

def post_detail(request,id):
	try:
		post = Post.objects.get(id=id)
	except Post.DoesNotExist:
		raise Http404('Post not found')
	return render(request,'post_detail.html',{'post':post})

