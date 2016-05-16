from .models import Idea, Outstanding
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group


class MyAdminSite(AdminSite):
    site_header = "Hackatrix Backend"
    site_title = "Hackatrix Backend"
    index_title = "Administrator"


class IdeaAdmin(admin.ModelAdmin):
    list_display = ('name', 'votes', 'description', 'register', 'is_active')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'register', None) is None:
            obj.register = request.user
        obj.save()


class OutstandingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment', 'register')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'register', None) is None:
            obj.register = request.user
        obj.save()


admin_site = MyAdminSite(name='myadmin')
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
admin_site.register(Idea, IdeaAdmin)
admin_site.register(Outstanding, OutstandingAdmin)
