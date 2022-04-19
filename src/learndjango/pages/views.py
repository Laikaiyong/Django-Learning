from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    home_context = {
        'title': 'Home'
    }
    return render(request, 'home.html', home_context)

def contact_view(request, *args, **kwargs):
    contact_context = {
        'title': 'Contact',
        'html': '<kbd>Esc</kbd>'
    }
    return render(request, 'contact.html', contact_context)

def about_view(request, *args, **kwargs):
    about_context = {
        'title': 'About',
        'developers': ['Vandyck', 'Vandaik', 'Vandyke']
    }
    return render(request, 'about.html', about_context)