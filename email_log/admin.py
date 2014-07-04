from django.contrib import admin

from .models import Email


BODY_FRAME = """\
<iframe id="html_body" width='800' height='600'></iframe>
<script>
    if(!$){{$ = django.jQuery;}}
    $('#html_body').get()[0].contentWindow.document.write('{}');
</script>
""".replace('\n', '')

class EmailAdmin(admin.ModelAdmin):
    list_display = ['recipients', 'from_email', 'subject', 'date_sent', 'ok']
    list_display_links = ['subject',]
    list_filter = ['date_sent', 'ok']
    fields = ['recipients', 'from_email', 'subject', '_html_body', 'date_sent', 'ok']
    readonly_fields = ['from_email', 'recipients', 'subject', 'body',
                       '_html_body', 'date_sent', 'ok']
    search_fields = ['subject', 'body', 'recipients']

    def has_delete_permission(self, *args, **kwargs):
        return False

    def has_add_permission(self, *args, **kwargs):
        return False

    def _html_body(self, obj):
        escaped = obj.html_body.replace("'", r"\'")
        return BODY_FRAME.format(escaped)

    _html_body.short_description = 'HTML body'
    _html_body.allow_tags = True


admin.site.register(Email, EmailAdmin)
