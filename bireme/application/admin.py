from django.contrib import admin
from models import *

class GenericAdmin(admin.ModelAdmin):

    exclude = ('updated', 'updater')
    list_display = ['__unicode__', 'creator', 'created']
    search_fields  = ['__unicode__',]

class GenericStackedAdmin(admin.StackedInline):
    exclude = ('updated', 'updater')

class VersionStackedAdmin(GenericStackedAdmin):
    model = Version 
    extra = 0 

class ApplicationAdmin(GenericAdmin):
    list_display = ('name', 'creator', 'created')
    inlines = [VersionStackedAdmin, ]

admin.site.register(Application, ApplicationAdmin)