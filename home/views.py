from django.views import generic

class LandingPage(generic.TemplateView):
    template_name = 'index.html'
