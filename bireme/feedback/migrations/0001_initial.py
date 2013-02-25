# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Objective'
        db.create_table('feedback_objective', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 25, 18, 17, 45, 166627))),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 25, 18, 17, 45, 166662))),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='+', null=True, blank=True, to=orm['auth.User'])),
            ('updater', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='+', null=True, blank=True, to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('is_another', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('feedback', ['Objective'])

        # Adding model 'SimilarSite'
        db.create_table('feedback_similarsite', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 25, 18, 17, 45, 166627))),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 25, 18, 17, 45, 166662))),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='+', null=True, blank=True, to=orm['auth.User'])),
            ('updater', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='+', null=True, blank=True, to=orm['auth.User'])),
            ('feedback', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedback.Feedback'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('feedback', ['SimilarSite'])

        # Adding model 'Category'
        db.create_table('feedback_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 25, 18, 17, 45, 166627))),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 25, 18, 17, 45, 166662))),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='+', null=True, blank=True, to=orm['auth.User'])),
            ('updater', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='+', null=True, blank=True, to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('feedback', ['Category'])

        # Adding model 'Feedback'
        db.create_table('feedback_feedback', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 25, 18, 17, 45, 166627))),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 25, 18, 17, 45, 166662))),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='+', null=True, blank=True, to=orm['auth.User'])),
            ('updater', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='+', null=True, blank=True, to=orm['auth.User'])),
            ('problem', self.gf('django.db.models.fields.TextField')()),
            ('blocker_error', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['application.Application'])),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('referer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('site', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('hash', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('is_error', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('staff_comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('answer', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedback.Category'], null=True, blank=True)),
        ))
        db.send_create_signal('feedback', ['Feedback'])

        # Adding model 'AditionalFeedback'
        db.create_table('feedback_aditionalfeedback', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 25, 18, 17, 45, 166627))),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 25, 18, 17, 45, 166662))),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='+', null=True, blank=True, to=orm['auth.User'])),
            ('updater', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='+', null=True, blank=True, to=orm['auth.User'])),
            ('objective', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedback.Objective'], null=True, blank=True)),
            ('regular_user', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('how_should_work', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('another_objective', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('feedback', ['AditionalFeedback'])


    def backwards(self, orm):
        
        # Deleting model 'Objective'
        db.delete_table('feedback_objective')

        # Deleting model 'SimilarSite'
        db.delete_table('feedback_similarsite')

        # Deleting model 'Category'
        db.delete_table('feedback_category')

        # Deleting model 'Feedback'
        db.delete_table('feedback_feedback')

        # Deleting model 'AditionalFeedback'
        db.delete_table('feedback_aditionalfeedback')


    models = {
        'application.application': {
            'Meta': {'object_name': 'Application'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 25, 18, 17, 45, 166627)'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'responsible': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 25, 18, 17, 45, 166662)'}),
            'updater': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'feedback.aditionalfeedback': {
            'Meta': {'object_name': 'AditionalFeedback'},
            'another_objective': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 25, 18, 17, 45, 166627)'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"}),
            'how_should_work': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'objective': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['feedback.Objective']", 'null': 'True', 'blank': 'True'}),
            'regular_user': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 25, 18, 17, 45, 166662)'}),
            'updater': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"})
        },
        'feedback.category': {
            'Meta': {'object_name': 'Category'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 25, 18, 17, 45, 166627)'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 25, 18, 17, 45, 166662)'}),
            'updater': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"})
        },
        'feedback.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'answer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['application.Application']"}),
            'blocker_error': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['feedback.Category']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 25, 18, 17, 45, 166627)'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"}),
            'hash': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_error': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'problem': ('django.db.models.fields.TextField', [], {}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'staff_comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 25, 18, 17, 45, 166662)'}),
            'updater': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'feedback.objective': {
            'Meta': {'object_name': 'Objective'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 25, 18, 17, 45, 166627)'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_another': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 25, 18, 17, 45, 166662)'}),
            'updater': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"})
        },
        'feedback.similarsite': {
            'Meta': {'object_name': 'SimilarSite'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 25, 18, 17, 45, 166627)'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"}),
            'feedback': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['feedback.Feedback']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 25, 18, 17, 45, 166662)'}),
            'updater': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['feedback']
