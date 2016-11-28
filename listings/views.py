from django.http import HttpResponse
from django.shortcuts import render
from .models import Listing
from .forms import ListingForm
import datetime


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
    form_class = ListingForm
    form = form_class(request.POST or None)
    if request.method == "POST":

        if form.is_valid():
            listing = form.save(commit=False)
            listing.team_member = form.cleaned_data['team_member']
            listing.address = form.cleaned_data['address']
            listing.list_price = form.cleaned_data['list_price']
            listing.commission_rate = form.cleaned_data['commission_rate']
            listing.commission_value = form.cleaned_data['commission_value']
            listing.date_listed = datetime.datetime.now()

            listing.save()
            # return redirect('sales')
        else:
            form = ListingFormForm()
    return render(request, 'listings/listing_new.html', {'form': form})
