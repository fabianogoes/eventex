# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Media.media_doc'
        db.add_column(u'core_media', 'media_doc',
                      self.gf('django.db.models.fields.CharField')(default=3, max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Media.media_doc'
        db.delete_column(u'core_media', 'media_doc')


    models = {
        u'core.contact': {
            'Meta': {'object_name': 'Contact'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Speaker']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.course': {
            'Meta': {'object_name': 'Course', '_ormbases': [u'core.Talk']},
            'notes': ('django.db.models.fields.TextField', [], {}),
            'slots': ('django.db.models.fields.IntegerField', [], {}),
            u'talk_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Talk']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'core.media': {
            'Meta': {'object_name': 'Media'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'media_doc': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'media_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'talk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Talk']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'core.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'core.talk': {
            'Meta': {'object_name': 'Talk'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'speakers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Speaker']", 'symmetrical': 'False'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['core']