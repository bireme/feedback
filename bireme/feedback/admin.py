from django.contrib import admin
from models import *
from util.models import *

class GenericAdmin(admin.ModelAdmin):
    
    exclude = ('updated', 'updater')
    list_display = ['__unicode__', 'creator', 'created']
    search_fields  = ['__unicode__',]
    

admin.site.register(Objective, GenericAdmin)
admin.site.register(SimilarSite, GenericAdmin)
admin.site.register(Feedback, GenericAdmin)
admin.site.register(AditionalFeedback, GenericAdmin)
admin.site.register(Category, GenericAdmin)
admin.site.register(Country)