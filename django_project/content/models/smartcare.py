# coding: utf-8
from datetime import datetime

__author__ = 'Alison Mukoma <AMukoma@brhc.com>'
__revision__ = ':%H$'
__date__ = ('%s' % (datetime.now()))
__license__ = ''
__copyright__ = 'Broadreach Corperation'


from django.db import models
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField


class Overview(models.Model):
    title = models.CharField(
       _('Title'),
       max_length=255,
       null=True,
       blank=True
        )
    published = models.BooleanField(default=False)
    content = RichTextField(
        _("Content"),
        null=True,
        blank=True
        )
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class FunctionalModules(models.Model):
    title = models.CharField(
       _('Title'),
       max_length=255,
       null=True,
       blank=True
        )
    content = RichTextField(
            _("Content"),
        null=True,
        blank=True
        )
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TechnologyStack(models.Model):
    title = models.CharField(
       _('Title'),
       max_length=255,
       null=True,
       blank=True
        )
    content = RichTextField(
            _("Content"),
        null=True,
        blank=True
        )
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class DevelopmentPipeline(models.Model):
    title = models.CharField(
       _('Title'),
       max_length=255,
       null=True,
       blank=True
        )
    content = RichTextField(
            _("Content"),
        null=True,
        blank=True
        )
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TechnicalUpdates(models.Model):
    title = models.CharField(
       _('Title'),
       max_length=255,
       null=True,
       blank=True
        )
    content = RichTextField(
            _("Content"),
        null=True,
        blank=True
        )
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Deployment(models.Model):
    title = models.CharField(
       _('Title'),
       max_length=255,
       null=True,
       blank=True
        )
    content = RichTextField(
            _("Content"),
        null=True,
        blank=True
        )
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Training(models.Model):
    title = models.CharField(
       _('Title'),
       max_length=255,
       null=True,
       blank=True
        )
    content = RichTextField(
            _("Content"),
        null=True,
        blank=True
    )
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProjectSummery(models.Model):
    title = models.CharField(
        _('Summery Title'),
        max_length=255,
        null=True,
        blank=True
    )
    content = RichTextField(
        _("What user will quickly read on home page summery about SmartCare"),
        null=True,
        blank=True
        )
    published = models.BooleanField(default=True)
    active_on_site = models.BooleanField(
        _('Is it the one you want to use on the home page?'),
        default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Summery'
        verbose_name_plural = 'Summeries'
        ordering = ['created']
    def __str__(self):
        return self.title



class Hub(models.Model):
    name = models.CharField(
        _('Hub Name'),
        max_length=255,
        null=True,
        blank=True
    )
    content = RichTextField(
        _("Details about this Hub that you want to share with public."),
        null=True,
        blank=True
        )
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Hub'
        verbose_name_plural = 'Hubs'
        ordering = ['-created']
    def __str__(self):
        return self.name
