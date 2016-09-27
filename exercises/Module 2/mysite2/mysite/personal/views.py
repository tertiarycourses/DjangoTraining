from django.shortcuts import render

def index(request):
	return render(request,'personal/home.html')

def contact(request):
	return render(request,'personal/contact.html',{'contactinfo': ["Tel:12345678","Email:test@test.com"] })