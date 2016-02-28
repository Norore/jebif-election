
from django.conf.urls import *
from django.views.generic import TemplateView

from election.views import *

urlpatterns = patterns('',
	('^(?P<election_id>\d+)/$', vote),
	('^(?P<election_id>\d+)/ok/$', TemplateView.as_view(template = "election/vote-ok.html")),
	('^(?P<election_id>\d+)/results/$', results),
	('^(?P<election_id>\d+)/mailing/$', mailing),
)

