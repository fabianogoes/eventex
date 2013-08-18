# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Talk

class TalkDetailTest(TestCase):
    def setUp(self):
        t = Talk.objects.create(title='Talk', start_time='10:00')
        t.speakers.create(name=u'Fabiano Góes', slug='fabiano-goes')
        self.resp = self.client.get(r('core:talk_detail', args=[1]))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)
 
    def test_template(self):
        'Template should be core/talk_detail.html'
        self.assertTemplateUsed(self.resp, 'core/talk_detail.html')

    def test_talk_in_context(self):
        talk = self.resp.context['talk']
        self.assertIsInstance(talk, Talk)

    def test_not_found(self):
        response = self.client.get(r('core:talk_detail', args=[0]))
        self.assertEqual(404, response.status_code)

    """
     Código refatorado, foi criado as properties:
       videos e slides na model Talk
    """    
    #def test_videos_in_context(self):
    #    self.assertIn('videos', self.resp.context)

    #def test_slides_in_context(self):
    #    self.assertIn('slides', self.resp.context)  

    def test_html(self):
        self.assertContains(self.resp, 'talk')
        self.assertContains(self.resp, '/palestrantes/fabiano-goes/')
        self.assertContains(self.resp, u'Fabiano Góes')
