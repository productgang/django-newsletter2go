#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-newsletter2go
------------

Tests for `django-newsletter2go` models backends.
"""

from django.core.mail import send_mail
from django.test import TestCase

import responses


class Newsletter2GoBackendTests(TestCase):
    @responses.activate
    def test_send_success(self):
        responses.add(responses.POST,
                      'https://www.newsletter2go.de/de/api/send/email/',
                      body='{"status": 200}', status=200,
                      content_type='application/json')
        with self.settings(
                EMAIL_BACKEND='newsletter2go.backends.Newsletter2GoEmailBackend',
                NEWSLETTER2GO_API_KEY='asdf'):
            sent_mails = send_mail(
                'Subject', 'Message', 'from@domain.tld', ['to@domain.tld'],
                fail_silently=False
            )
        self.assertEqual(sent_mails, 1)

    @responses.activate
    def test_send_fail(self):
        responses.add(responses.POST,
                      'https://www.newsletter2go.de/de/api/send/email/',
                      body='{"status": 401}', status=200,
                      content_type='application/json')
        with self.settings(
                EMAIL_BACKEND='newsletter2go.backends.Newsletter2GoEmailBackend',
                NEWSLETTER2GO_API_KEY='asdf'):
            sent_mails = send_mail(
                'Subject', 'Message', 'from@domain.tld', ['to@domain.tld'],
                fail_silently=False
            )
        self.assertEqual(sent_mails, 0)
