from django.core.mail import get_connection, EmailMultiAlternatives
from django.core.mail.backends.base import BaseEmailBackend

from .conf import settings
from .models import Email


class EmailBackend(BaseEmailBackend):

    """Wrapper email backend that records all emails in a database model"""

    def __init__(self, **kwargs):
        super(EmailBackend, self).__init__(**kwargs)
        self.connection = get_connection(settings.EMAIL_LOG_BACKEND, **kwargs)

    def send_messages(self, email_messages):
        num_sent = 0
        for message in email_messages:
            recipients = '; '.join(message.to)
            if isinstance(message, EmailMultiAlternatives):
                try:
                    html_body = filter(
                        lambda item: item[1] == 'text/html',
                        message.alternatives,
                    )[0][0]
                except IndexError:
                    html_body = ''
            else:
                html_body = ''
            email = Email.objects.create(
                from_email=message.from_email,
                recipients=recipients,
                subject=message.subject,
                body=message.body,
                html_body=html_body,
            )
            message.connection = self.connection
            num_sent += message.send()
            if num_sent > 0:
                email.ok = True
                email.save()
        return num_sent
