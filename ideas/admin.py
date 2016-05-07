from .models import Idea, Outstanding
from django.contrib import admin


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


admin.site.register(Idea, IdeaAdmin)
admin.site.register(Outstanding, OutstandingAdmin)
