# coding: utf-8
from datetime import datetime

__author__ = 'Alison Mukoma <AMukoma@brhc.com>'
__revision__ = ':%H$'
__date__ = ('%s' % (datetime.now()))
__license__ = ''
__copyright__ = 'Broadreach Corperation'

import random
from django.views.generic import TemplateView

from ..models.aboutus import AboutUs, Foreword
from ..models.success_story import SuccessStory
from ..models.sponsors import Partner
from ..models.smartcare import ProjectSummery


class HomeView(TemplateView):
    template_name = 'content/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        success_qs = SuccessStory.objects.filter(published=True)[:3]
        context['recent_stories'] = success_qs

        partner_qs = Partner.objects.filter(partner_type="PT")
        sponsor_qs = Partner.objects.filter(partner_type="SP")
        partner_list = list(partner_qs)
        sponsor_list = list(sponsor_qs)
        try:
            random_partners = list(random.sample(partner_list,
                                               len(partner_list)))
            random_sponsors = list(random.sample(sponsor_list,
                                               len(sponsor_list)))
            foreword_qs = Foreword.objects.get(active=True)
            project_overview = ProjectSummery.objects.get(active_on_site=True)

        except:
            random_partners = []
            random_sponsors = []
            foreword_qs = ''
            project_overview = ''

        context['foreword'] = foreword_qs
        context['partners'] = random_partners
        context['sponsors'] = random_sponsors
        context['summery'] = project_overview

        return context


class AboutUsView(TemplateView):
    template_name = 'content/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        try:
            aboutus_qs = []
            foreword_qs = []
        except:
            aboutus_qs = ''
            foreword_qs = ''
        context['aboutus'] = ''
        context['foreword'] = []

        return context
