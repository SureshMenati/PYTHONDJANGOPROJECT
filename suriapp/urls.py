"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from suriapp import views
app_name='suriapp'


urlpatterns = [
     path('about.html', views.about, name='about.html'),
     path('event_details.html', views.event_details, name='event_details.html'),
     path('index.html', views.index, name='index.html'),
     path('rent_venue.html', views.rent_venue, name='rent_venue.html'),
     path('shows_events.html', views.shows_events, name='shows_events.html'), 
     path('ticket_details.html', views.ticket_details, name='ticket_details.html'),
     path('tickets.html', views.tickets, name='tickets.html'),
    
    
]     