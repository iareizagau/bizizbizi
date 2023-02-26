from django.contrib import admin
from .models import BikeSpot, Country, OpenWeatherMap, Warmshower, GpsTrackingData
from .models import GpsTracks, Icon, PointsInterest
#from .models import Image, Product


class CountryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class BikeSpotAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ("title", "created", "order",)
    search_fields = ("title",)
    date_hierarchy = "updated"
    list_filter = ("town",)


class OpenWeatherMapAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class WarmshowerAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class GpsTracksAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class IconAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PointsInterestAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class GpsTrackingDataAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(BikeSpot, BikeSpotAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(OpenWeatherMap, OpenWeatherMapAdmin)
admin.site.register(Warmshower, WarmshowerAdmin)
admin.site.register(GpsTracks, GpsTracksAdmin)
admin.site.register(Icon, IconAdmin)
admin.site.register(PointsInterest, PointsInterestAdmin)
admin.site.register(GpsTrackingData, GpsTrackingDataAdmin)
#admin.site.register(Image, ImageAdmin)
#admin.site.register(Product, ProductAdmin)
