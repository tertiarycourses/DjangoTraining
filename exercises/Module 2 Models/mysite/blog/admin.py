from django.contrib import admin
from .models import Post

@admin.register(Post)
class PetAdmin(admin.ModelAdmin):
	list_display = ['title', 'body', 'date']
