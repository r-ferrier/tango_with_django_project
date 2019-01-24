from django.contrib import admin
from rango.models import Category, Page

# Register your models here.


class Pages(admin.ModelAdmin):
    # fields = ['title', 'category', 'url', 'views']
    list_display = ('title', 'category', 'url')


admin.site.register(Category)
admin.site.register(Page, Pages)
