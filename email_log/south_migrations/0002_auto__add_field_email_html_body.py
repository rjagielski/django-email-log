# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Email.html_body'
        db.add_column(u'email_log_email', 'html_body',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Email.html_body'
        db.delete_column(u'email_log_email', 'html_body')


    models = {
        u'email_log.email': {
            'Meta': {'ordering': "(u'-date_sent',)", 'object_name': 'Email'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_sent': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'from_email': ('django.db.models.fields.TextField', [], {}),
            'html_body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ok': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'recipients': ('django.db.models.fields.TextField', [], {}),
            'subject': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['email_log']