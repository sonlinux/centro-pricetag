# coding: utf-8
from datetime import datetime

__author__ = 'Alison Mukoma <mukomalison@gmail.com>'
__revision__ = ':%H$'
__date__ = ('%s' % (datetime.now()))
__doc__ = ''
__license__ = ''
__copyright__ = ''

from django.conf.urls import url
from .views.home import HomeView
from .views.home import AboutUsView
from .views.success_story import (
    SuccessStoryList,
    SuccessStoryDetail)
from .views.under_development import UnderDevelopment
from .views.download_smartcare import DownloadFile

from .views.smartcare import (
    OverviewView,
    FunctionalModulesView,
    TechnologyStackView,
    DevelopmentPipelineView,
    TechnicalUpdatesView,
    DeploymentView,
    TrainingView
    )
from .views.sponsors import SponsorPartnerView


urlpatterns = [
    url(r'^$',
        HomeView.as_view(),
        name='home'),

    url(r'^overview/$',
        OverviewView.as_view(),
        name='overview'),

    url(r'^sponsors/$',
        SponsorPartnerView.as_view(),
        name='sponsorship'),

    url(r'^functional-modules$',
        FunctionalModulesView.as_view(),
        name='functional_modules'),

    url(r'^technology-stack/$',
        TechnologyStackView.as_view(),
        name='technology_stack'),

    url(r'^deployment-pipeline/$',
        DevelopmentPipelineView.as_view(),
        name='deployment_pipeline'),

    url(r'^technical-updates/$',
        TechnicalUpdatesView.as_view(),
        name='technical_updates'),

    url(r'^deployment$',
        DeploymentView.as_view(),
        name='deployment'),

    url(r'^training/$',
        TrainingView.as_view(),
        name='training'),

    url(r'^download/$',
        DownloadFile.as_view(),
        name='download'),
    url(r'^under-development/$',
        UnderDevelopment.as_view(),
        name='under_development'),
    url(r'^about/$',
        AboutUsView.as_view(),
        name='about'),
    url(r'^success/$',
        SuccessStoryList.as_view(),
        name='success'),
    url(r'^story/(?P<story_pk>\d+)/detail/$',
        SuccessStoryDetail.as_view(),
        name='success_detail')
]
