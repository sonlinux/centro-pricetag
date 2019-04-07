# coding: utf-8
from datetime import datetime


__author__ = 'Alison Mukoma <AMukoma@brhc.com>'
__revision__ = ':%H$'
__date__ = ('%s' % (datetime.now()))
__license__ = ''
__copyright__ = 'Broadreach Corperation'


from ..models.smartcare import Hub

from django.views.generic import TemplateView

from ..models.sponsors import Partner

class SponsorPartnerView(TemplateView):
    template_name = 'content/sponsor_partner_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SponsorPartnerView, self).get_context_data(**kwargs)
        try:
            hubs_qs = Hub.objects.filter(published=True)
            orgnanisation_qs = Partner.objects.all()
        except:
            hubs_qs = ''
            orgnanisation_qs = ''

        context['hubs'] = hubs_qs
        context['orgs'] = orgnanisation_qs

        return context

