# -*- coding: utf-8 -*-

from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail.message import sanitize_address
from django.conf import settings

import requests


class Newsletter2GoEmailBackend(BaseEmailBackend):
    n2g_api_endpoint = 'https://www.newsletter2go.de/de/api/send/email/'

    def send_messages(self, emails):
        """
        Sends one or more EmailMessage objects and returns the number of email
        messages sent.
        """
        if not emails:
            return

        num_sent = 0

        for email in emails:
            if not email.recipients():
                continue
            from_email = sanitize_address(email.from_email, email.encoding)
            recipients = [sanitize_address(addr, email.encoding)
                          for addr in email.recipients()]

            for recipient in recipients:
                payload = {
                    'key': settings.NEWSLETTER2GO_API_KEY,
                    'to': recipient,
                    'from': from_email,
                    'subject': email.subject,
                    'linktracking': int(getattr(settings, 'NEWSLETTER2GO_LINKTRACKING', True)),
                    'opentracking': int(getattr(settings, 'NEWSLETTER2GO_OPENTRACKING', True)),
                }
                payload['html' if email.content_subtype == 'html' else 'text'] = email.body
                response = requests.post(self.n2g_api_endpoint, payload)

                response_json = response.json()

                if response_json.get('status') == 200:
                    num_sent += 1

        return num_sent
