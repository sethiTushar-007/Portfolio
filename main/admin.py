from django.contrib import admin
from django.contrib.sites.models import Site
from .models import *

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)

class JobTitleAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'is_active',)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'is_active',)

class SocialIconAdmin(admin.ModelAdmin):
    list_display = ('order', 'fontawesome_icon', 'is_active',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(JobTitle, JobTitleAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(SocialIcon, SocialIconAdmin)

admin.site.unregister(Site)
class SiteAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'domain')
    readonly_fields = ('id',)
    list_display = ('id', 'name', 'domain')
    list_display_links = ('name',)
    search_fields = ('name', 'domain')
admin.site.register(Site, SiteAdmin)