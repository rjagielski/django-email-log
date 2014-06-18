from django.contrib import admin

from .models import Email


class EmailAdmin(admin.ModelAdmin):
    list_display = ['recipients', 'from_email', 'subject', 'date_sent', 'ok']
    list_filter = ['date_sent', 'ok']
    readonly_fields = ['from_email', 'recipients', 'subject', 'body',
                       '_html_body', 'date_sent', 'ok']
    search_fields = ['subject', 'body', 'recipients']
    exclude = ['html_body']

    def has_delete_permission(self, *args, **kwargs):
        return False

    def has_add_permission(self, *args, **kwargs):
        return False

    def _html_body(self, obj):
        return "<iframe width='800' height='600'></iframe><script>$('iframe').get()[0].contentWindow.document.write('" + obj.html_body + "');</script>"
    _html_body.short_description = 'HTML body'
    _html_body.allow_tags = True


admin.site.register(Email, EmailAdmin)
