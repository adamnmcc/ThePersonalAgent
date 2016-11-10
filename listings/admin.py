from django.contrib import admin

# Register your models here.
from .models import Listing, Team, Site

admin.site.register(Listing)
admin.site.register(Team)
admin.site.register(Site)
