from django.contrib import admin
from .models import Skill, Author, Category, Testimony, Work, Item, Service, Message


class ItemInline(admin.TabularInline):
    model = Item


class ServiceAdmin(admin.ModelAdmin):
    inlines = [ItemInline]



admin.site.register(Category)
admin.site.register(Testimony)
admin.site.register(Skill) 
admin.site.register(Service, ServiceAdmin)
admin.site.register(Author)
admin.site.register(Work)
admin.site.register(Item)
admin.site.register(Message)