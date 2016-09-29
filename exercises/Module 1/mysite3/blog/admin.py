from django.contrib import admin
from blog.models import Post

class postAdmin(admin.ModelAdmin):
	list_display = ['title','date']

admin.site.register(Post,postAdmin)

