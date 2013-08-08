# coding: utf-8

from django.test import TestCase
from mock import Mock
from eventex.subscriptions.admin import SubscriptionAdmin, Subscription, admin

class MarkAsPaidTest(TestCase):
    def setUp(self):
        'Instancia o modelo admin'
        self.model_admin = SubscriptionAdmin(Subscription, admin.site)

        'popula o banco'
        Subscription.objects.create(name='Fabiano Góes', cpf='12345678901',
                                    email='fabianogoes@gmail.com')

    def test_has_action(self):
        'Action is instaled'
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        'Mark all as paid'
        fake_request = Mock()
        queryset = Subscription.objects.all()
        self.model_admin.mark_as_paid(fake_request, queryset)

        self.assertEqual(1, Subscription.objects.filter(paid=True).count())