# coding: utf-8
from datetime import datetime

__author__ = 'Alison Mukoma <AMukoma@brhc.com>'
__revision__ = ':%H$'
__date__ = ('%s' % (datetime.now()))
__license__ = ''
__copyright__ = 'Broadreach Corperation'

from django.views.generic import ListView, DetailView

from ..models.success_story import SuccessStory
from ..models.category import Category

class SuccessStoryList(ListView):
    template_name = 'content/success_stories_list.html'
    model = SuccessStory

    def get_context_data(self, **kwargs):
        context = super(SuccessStoryList, self).get_context_data(**kwargs)

        success_qs = SuccessStory.objects.filter(published=True)
        recent_success_qs = SuccessStory.objects.filter(published=True)[:5]

        category_qs = Category.objects.all()[:5]
        context['categories'] = category_qs
        context['success_stories'] = success_qs
        context['recent_stories'] = recent_success_qs

        return context


class SuccessStoryDetail(ListView):

    template_name = 'content/success_story_detail.html'
    model = SuccessStory

    def get_context_data(self, **kwargs):
        context = super(SuccessStoryDetail, self).get_context_data(**kwargs)

        self.story_pk = self.kwargs.get('story_pk', None)
        self.story_qs = SuccessStory.objects.get(pk=self.story_pk)
        context['story'] = self.story_qs

        return context


