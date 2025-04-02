from django.contrib import admin

from .models import Band
from .models import Listing

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'year_formed', 'active')

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'sold', 'year', 'type', 'band')
    list_filter = ('band',)
    search_fields = ('title', 'description')


admin.site.register(Band, BandAdmin)
admin.site.register(Listing)
