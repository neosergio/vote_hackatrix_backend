from .models import Idea
from django.contrib import admin


class IdeaAdmin(admin.ModelAdmin):
    list_display = ('name', 'votes', 'description')


admin.site.register(Idea, IdeaAdmin)