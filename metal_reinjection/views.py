""" System Module """
from django.shortcuts import render


def page_not_found_view(request, exception):
    data = {}
    return render(request, 'templates/404.html', data)


def custom_500_error_view(request,  exception):
    data = {}
    return render(request, 'templates/500.html', data)
