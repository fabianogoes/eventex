# coding: utf-8

from django.test import TestCase
from datetime import datetime
from django.db import IntegrityError
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name=u'Fabiano Góes',
            cpf='12345678901',
            email='fabianogoes@gmail.com',
            phone='11-55556666'
        )

    def test_create(self):
        'Subscription must have name, cpf, email, phone'
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_has_created_at(self):
        'Subscription must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Fabiano Góes', unicode(self.obj))


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        Subscription.objects.create(name=u'Fabiano Góes', cpf='12345678901',
                                    email='fabianogoes@gmail.com', phone='11-98761234')


    def test_cpf_unique(self):
        'CPF must be unique'
        s = Subscription(name=u'Fabiano Góes', cpf='12345678900',
                         email='outroemail@gmail.com', phone='11-98761234')
        self.assertRaises(IntegrityError, s.save())

    def test_email_unique(self):
        'Email must be unique'
        s = Subscription(name=u'Fabiano Góes', cpf='12345678900',
                         email='fabianogoes@gmail.com.br', phone='11-98761234')
        self.assertRaises(IntegrityError, s.save())