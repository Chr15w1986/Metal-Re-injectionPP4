""" Home app Views module """
from django.views import generic


class LandingPage(generic.TemplateView):
    """ loads template for main page """
    template_name = 'index.html'
