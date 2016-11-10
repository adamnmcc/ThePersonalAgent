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
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.team_member = request.team_member
            listing.address = request.address
            listing.list_price = request.list_price
            listing.commission_rate = request.commission_rate
            listing.commission_value = request.commission_value

            listing.save()
            # return redirect('sales')
        else:
            form = ListingFormForm()
    return render(request, 'listings/listing_new.html', {'form': form})
