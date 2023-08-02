from django.shortcuts import render

# Create your views here

def about(request):
    return render(request, 'about.html')

def event_details(request):
    return render(request, 'event-details.html')

def index(request):
    return render(request, 'index.html')

def rent_venue(request):
    return render(request, 'rent_venue.html')

def shows_events(request):
    return render(request, 'shows_events.html')

def ticket_details(request):
    return render(request, 'ticket_details.html')

def tickets(request):
    return render(request, 'tickets.html')






