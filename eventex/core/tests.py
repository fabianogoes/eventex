"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class HomepageTest(TestCase):
    def setUp(self):
        self.tearDown()
        self.resp = self.client.get('/')

    def test_get(self):
        'GET / must return status code 200.'
        response = self.client.get('/')
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Homepage must use template index.html'
        self.assertTemplateUsed(self.resp, 'index.html')
