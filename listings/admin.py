from django.contrib import admin

# Register your models here.
from .models import Team, Listing, Site

admin.site.register(Team)
admin.site.register(Site)
admin.site.register(Listing)
