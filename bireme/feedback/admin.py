from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from util.models import *
from models import *

class GenericAdmin(admin.ModelAdmin):
    
    exclude = ('updater', )
    list_display = ['__unicode__', 'creator', 'created']
    search_fields  = ['__unicode__',]
    readonly_fields = ('updated', )

class FeedbackAdmin(GenericAdmin):
    model = Feedback

    readonly_fields = ['problem', 'blocker_error', 'application', 'version', 'ip',
        'referer', 'site', 'is_error', 'created', ]

    fieldsets = (
        (_('Administrative'), {
            'fields' : ['is_active', 'staff_comment', 'answer', 'category'],
        }), 
        (_('Information'), {
            'fields' : ['problem', 'blocker_error', 'application', 'version', 'ip',
                'referer', 'site', 'is_error', 'created' ],
            # _('Administrative'): ['staff_comment', 'answer', 'is_valid'],
        }), 
    )

    list_display = ['id', 'category', 'has_answer', 'is_error', 'application', 'version', 'creator']
    list_filter = ['is_error', 'application', 'category']
    search_fields = ['id', 'problem', 'answer', 'problem']

    def has_answer(self, obj):
        if obj.answer:
            return True
        return False
    has_answer.admin_order_field = 'answer'
    has_answer.short_description = _("Has Answer?")
    has_answer.boolean = True

    
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(AditionalFeedback, GenericAdmin)
admin.site.register(Category, GenericAdmin)
admin.site.register(Country)