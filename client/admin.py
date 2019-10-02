from django.contrib import admin
from .models import Client, Packages, Tv

# Register your models here.


class ListingClient(admin.ModelAdmin):
    list_display = ('first_name', 'company_name', 'phone',
                    'package', 'tv_package', 'expire')
    list_filter = ('package', 'tv_package')
    search_fields = ('first_name', 'last_name',
                     'email', 'phone', 'company_name',)
    list_per_page = 25


class ListingPackages(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    list_per_page = 20


class ListingTv(admin.ModelAdmin):
    list_display = ('name', 'number_of_channels', 'price')
    search_fields = ('name',)
    list_per_page = 20


admin.site.register(Client, ListingClient)
admin.site.register(Packages, ListingPackages)
admin.site.register(Tv, ListingTv)
