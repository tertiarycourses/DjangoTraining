
from django.contrib import admin
from django.conf.urls import url


from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^post/(\d+)/', views.post_detail, name='post_detail'),
]

