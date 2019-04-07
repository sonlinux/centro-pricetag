# coding: utf-8
from datetime import datetime

__author__ = 'Alison Mukoma <AMukoma@brhc.com>'
__revision__ = ':%H$'
__date__ = ('%s' % (datetime.now()))
__license__ = ''
__copyright__ = 'Broadreach Corperation'

from django.views.generic import TemplateView

from ..models.smartcare import (
    Overview,
    FunctionalModules,
    TechnologyStack,
    DevelopmentPipeline,
    TechnicalUpdates,
    Deployment,
    Training,
    )

class OverviewView(TemplateView):
    template_name = 'content/overview.html'

    def get_context_data(self, **kwargs):
        context = super(OverviewView, self).get_context_data(**kwargs)
        try:
            qs = Overview.objects.get(published=True)
        except:
            qs = ''
        context['overview'] = qs

        return context


class FunctionalModulesView(TemplateView):
    template_name = 'content/functional_modules.html'

    def get_context_data(self, **kwargs):
        context = super(FunctionalModulesView, self).get_context_data(**kwargs)
        try:
            qs = FunctionalModules.objects.get(published=True)
        except:
            qs = ''
        context['functional_modules'] = qs

        return context



class TechnologyStackView(TemplateView):
    template_name = 'content/technology_stack.html'

    def get_context_data(self, **kwargs):
        context = super(TechnologyStackView, self).get_context_data(**kwargs)
        try:
            qs = TechnologyStack.objects.get(published=True)
        except:
            qs = ''
        context['technology_stack'] = qs

        return context



class DevelopmentPipelineView(TemplateView):
    template_name = 'content/development_pipeline.html'

    def get_context_data(self, **kwargs):
        context = super(DevelopmentPipelineView, self).get_context_data(**kwargs)
        try:
            qs = DevelopmentPipeline.objects.get(published=True)
        except:
            qs = ''
        context['development_pipeline'] = qs

        return context



class TechnicalUpdatesView(TemplateView):
    template_name = 'content/technical_updates.html'

    def get_context_data(self, **kwargs):
        context = super(TechnicalUpdatesView, self).get_context_data(**kwargs)
        try:
            qs = TechnicalUpdates.objects.get(published=True)
        except:
            qs = ''
        context['technical_updates'] = qs

        return context



class DeploymentView(TemplateView):
    template_name = 'content/deployment.html'

    def get_context_data(self, **kwargs):
        context = super(DeploymentView, self).get_context_data(**kwargs)
        try:
            qs = Deployment.objects.get(published=True)
        except:
            qs = ''
        context['deployment'] = qs

        return context



class TrainingView(TemplateView):
    template_name = 'content/training.html'

    def get_context_data(self, **kwargs):
        context = super(TrainingView, self).get_context_data(**kwargs)
        try:
            qs = Training.objects.get(published=True)
        except:
            qs = ''
        context['training'] = qs

        return context
