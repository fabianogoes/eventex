# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from eventex.core.managers import KindContactManager, PeriodManager

class Speaker(models.Model):
    name = models.CharField(_('Nome'), max_length=255)
    slug = models.SlugField(_('Slug'))
    url = models.URLField(_('Url'))
    description = models.TextField(_(u'Descrição'), blank=True)

    class Meta:
        verbose_name=_('palestrante')
        verbose_name_plural = _('palestrantes')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/palestrantes/%s/' % self.slug           

class Contact(models.Model):
    KINDS = (
        ('P', _('Telefone')),
        ('E', _('E-mail')),
        ('F', _('Fax')),
    )
    speaker = models.ForeignKey('Speaker', verbose_name=_('palestrante')) 
    kind = models.CharField(_('tipo'), max_length=1, choices=KINDS)
    value = models.CharField(_('valor'), max_length=255)    

    objects = models.Manager()
    emails = KindContactManager('E')
    phones = KindContactManager('P')
    faxes = KindContactManager('F')

    def __unicode__(self):
        return self.value   

    def get_absolute_url(self):
        return ('core:speaker_detail', (), {'slug': self.slug}) 

class Talk(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.TimeField(blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name=_('palestrante'))

    objects = PeriodManager()

    @property
    def videos(self):
        return self.media_set.filter(kind='YT')

    @property
    def slides(self):
        return self.media_set.filter(kind='SL')    

    class Meta:
        verbose_name=_('palestra')
        verbose_name_plural = _('palestras')
        
    def __unicode__(self):
        return self.title     

    def get_absolute_url(self):
        return '/palestra/%d/' % self.pk

class Course(Talk):
    slots = models.IntegerField()
    notes = models.TextField()

    objects = PeriodManager()

class CodingCourse(Course):
    class Meta:
        proxy = True
    
    def do_some_python_stuff(self):
        return "Let's hack! at %s" % self.title    

class Media(models.Model):
    MEDIAS = (
        ('YT', _('YouTube')),
        ('SL', _('SlideShare')),
    )
    talk = models.ForeignKey('Talk', verbose_name=_('palestra')) 
    kind = models.CharField(_('Tipo'), max_length=2, choices=MEDIAS)
    title = models.CharField(_(u'Título'), max_length=200)
    media_id = models.CharField(_('ID_Ref'), max_length=255)
    media_doc = models.CharField(_('Doc_Slide'), max_length=255, default="0")

    def __unicode__(self):
        return u'%s - %s' % (self.talk.title, self.title)        
