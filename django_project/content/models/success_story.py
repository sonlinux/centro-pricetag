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

from .category import Category


class Author(models.Model):
    name = models.CharField(
        _('Author Name'),
        max_length=255,
    )
    extra_info = RichTextField()

    def __str__(self):
        return self.name

class SuccessStory(models.Model):
    title = models.CharField(
        _('Story Title'),
        max_length=255,
    )

    content = RichTextField()
    photo = models.ImageField(
        _('Story Main Photo'),
        upload_to='success_stories/upload/%Y/%m/%d',
        null=True,
        blank=True
    )

    photo_1 = models.ImageField(
        _('Story Optional photo 1'),
        upload_to='success_stories/upload/%Y/%m/%d',
        blank=True,
        null=True
    )
    photo_2 = models.ImageField(
        _('Story Optional photo 2'),
        upload_to='success_stories/upload/%Y/%m/%d',
        blank=True,
        null=True
    )

    photo_3 = models.ImageField(
        _('Story Optional photo 3'),
        upload_to='success_stories/upload/%Y/%m/%d',
        blank=True,
        null=True
    )

    photo_4 = models.ImageField(
        _('Story Optional photo 4'),
        upload_to='success_stories/upload/%Y/%m/%d',
        blank=True,
        null=True
    )

    author = models.ForeignKey(
        Author,
        default='',
        on_delete=models.SET_DEFAULT)
    category = models.ForeignKey(
        Category,
        default='',
        on_delete=models.SET_DEFAULT)
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Success Story'
        verbose_name_plural = 'Success Strories'

    def __str__(self):
        return self.title

