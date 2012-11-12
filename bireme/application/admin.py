from django.contrib import admin
from models import *

class GenericAdmin(admin.ModelAdmin):

    exclude = ('updated', 'updater')
    list_display = ['__unicode__', 'creator', 'created']
    search_fields  = ['__unicode__',]

class GenericStackedAdmin(admin.StackedInline):
    exclude = ('updated', 'updater')

class ApplicationAdmin(GenericAdmin):
    list_display = ('name', 'creator', 'created')

admin.site.register(Application, ApplicationAdmin)