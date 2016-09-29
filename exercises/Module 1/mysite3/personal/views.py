from django.shortcuts import render

def index(request):
	return render(request,'personal/home.html')

def contact(request):
	return render(request,'personal/contact.html',{'contactinfo':['Tel:1234567','Email:test@test.com']})