from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, World. You have created your first Django page")