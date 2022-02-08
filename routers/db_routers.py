from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django.urls import reverse

class AuthRouter:
    route_app_labels = {'auth', 'sessions', 'admin'}
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None
    def db_for_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
            ):
            return True
        return None
    def allow_migrate(self, db, app_label, model_name = None, **hints):
        if app_label in self.route_app_labels:
            return db == 'users_db'
        return None

class School:
    route_app_labels = {'school.apps.SchoolConfig', 'auth', 'contenttypes'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'school_db'
        return None
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'school_db'
        return None
    def allow_migrate(self, db, app_label, model_name = None, **hints):
        if app_label in self.route_app_labels:
            return db == 'school_db'
        return None
    def allow_migrate(self, db, app_label, model_name = None, **hints):
        if app_label in self.route_app_labels:
            return db == 'school_db'
        return None
class Media:
    route_app_labels = {'media'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'media_db'
        return None
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'media_db'
        return None
    def allow_migrate(self, db, app_label, model_name = None, **hints):
        if app_label in self.route_app_labels:
            return db == 'media_db'
        return None
class EntCell:
    route_app_labels = {'entCell'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'entCell_db'
        return None
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'entCell_db'
        return None
    def allow_migrate(self, db, app_label, model_name = None, **hints):
        if app_label in self.route_app_labels:
            return db == 'entCell_db'
        return None
class vAssist:
    route_app_labels = {'entCell'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'vAssist_db'
        return None
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'vAssist_db'
        return None
    def allow_migrate(self, db, app_label, model_name = None, **hints):
        if app_label in self.route_app_labels:
            return db == 'vAssist_db'
        return None
