from django import forms
from django.forms import ModelForm

from .models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('team_member', 'address', 'list_price', 'commission_rate', 'commission_value',)
