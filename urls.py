
from django.conf.urls import *
from django.views.generic.simple import direct_to_template
from django.views.generic import TemplateView
from . import views
#from election.views import *

urlpatterns = patterns('',
	('^(?P<election_id>\d+)/$', views.vote),
	#('^(?P<election_id>\d+)/ok/$', TemplateView.as_view(template = "election/vote-ok.html")),
        ('^(?P<election_id>\d+)/ok/$', direct_to_template{'template': 'election/vote-ok.html'}),
	('^(?P<election_id>\d+)/results/$', views.results),
	('^(?P<election_id>\d+)/mailing/$', views.mailing)
)

