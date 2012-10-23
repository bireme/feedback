from django.contrib import admin
from models import *

class GenericAdmin(admin.ModelAdmin):
    exclude = ('updated', 'updater')
    list_display = ['__unicode__', 'creator', 'created']
    search_fields  = ['__unicode__',]

class AditionalFeedbackStackedAdmin(admin.StackedInline):
    model = AditionalFeedback
    exclude = ('updated', 'updater')

class FeedbackAdmin(GenericAdmin):
    inlines = [AditionalFeedbackStackedAdmin, ]

admin.site.register(Objective, GenericAdmin)
admin.site.register(SimilarSite, GenericAdmin)
admin.site.register(Feedback, FeedbackAdmin)

