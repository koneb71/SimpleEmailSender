import logging

from django.shortcuts import render
from django.views.generic import TemplateView

from app.send_email import Mailer
from simple_email.settings import MAILGUN_RECIPIENT
from .mailgun import get_logs

mail = Mailer()


class Index(TemplateView):
    template_name = 'app/index.html'

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        to_emails = [i for i in request.POST['email_address'].split(',')]
        subject = request.POST['subject']
        body = request.POST['body']
        context = {'body': body, 'user': 'Admin'}
        success = False

        if to_emails and body:
            mail.send_messages(subject=subject,
                               template='email_templates/email.html',
                               context=context,
                               to_emails=to_emails)
            success = True
        return render(request, self.template_name, {'success': success})


class History(TemplateView):
    template_name = 'app/history.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        url = self.request.GET.get('url')
        context['logs'] = get_logs(url)
        context['recipient'] = MAILGUN_RECIPIENT
        return context