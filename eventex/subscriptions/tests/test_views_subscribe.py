# coding: utf-8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r


class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('subscriptions:subscribe'))

    def test_get(self):
        'Get /inscricao/ must return statuc code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Reponse should be a rendered template'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        'Html must contain input controls'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 7)
        self.assertContains(self.resp, 'type="text"', 5)
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        'HTML must contain csrf token.'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        'Context must have the subscription form'
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name=u'Fabiano Góes', cpf='12345678901',
                    email='fabianogoes@gmail.com', phone='15-12121212')
        self.resp = self.client.post(r('subscriptions:subscribe'), data)

    def test_post(self):
        'Valid POST should redirect to /inscricao/'
        self.assertEqual(302, self.resp.status_code)

    def test_save(self):
        'Valid POST must be saved'
        self.assertTrue(Subscription.objects.exists())

class SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        data = dict(nome=u'Fabiano Góes', cpf='00000000001',
                    email='fabianogoes@gmail.com', phone='11-55554444')
        self.resp = self.client.post(r('subscriptions:subscribe'), data)
    def test_post(self):
        'Invalid POST should not redirect.'
        self.assertEqual(200, self.resp.status_code)

    def test_form_errors(self):
        'Form must contain errors'
        self.assertTrue(self.resp.context['form'].errors)

    def test_dont_save(self):
        'Do not save data'
        self.assertFalse(Subscription.objects.exists())

class TemplateregressionTest(TestCase):
    def test_template_has_non_fields_errors(self):
        'Check if non_field_errors are shown in template'
        invalid_data = dict(name=u'Fabiano Góes', cpf='12345678901')
        response = self.client.post(r('subscriptions:subscribe'), invalid_data)
        self.assertContains(response, '<ul class="errorlist">')