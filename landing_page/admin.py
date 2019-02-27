from django.contrib import admin
from landing_page.models import BlogStuff, Profile

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'post_image']

admin.site.register(BlogStuff, BlogAdmin)
admin.site.register(Profile)
