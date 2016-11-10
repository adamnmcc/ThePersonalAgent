from django.http import HttpResponse
from django.shortcuts import render
from .models import Listing
from .forms import ListingForm

def index(request):
    return HttpResponse("Hello, world. You're at the Listings index.")

def sales(request):
    sales = Listing.objects.order_by('date_listed')
    return render(request, 'listings/sales.html', {'sales': sales}, {})

def exchanged(request):
    return render(request, 'listings/exchanged.html', {})

def fallen_through(request):
    return render(request, 'listings/fallen_through.html', {})


def listing_new(request):
    form = ListingForm()
    return render(request, 'listings/listing_new.html', {'form': form})
