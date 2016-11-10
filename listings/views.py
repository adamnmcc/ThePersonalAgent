from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the Listings index.")

def sales(request):
    return render(request, 'listings/sales.html', {})

def exchanged(request):
    return render(request, 'listings/exchanged.html', {})

def fallen_through(request):
    return render(request, 'listings/fallen_through.html', {})