from django.db import models
from ckeditor.fields import RichTextField


class Country(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        ordering = ["created"]

    def __str__(self):
        return self.name


# Create your models here.
class BikeSpot(models.Model):
    order = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.CASCADE)
    town = models.CharField(max_length=200, null=True, blank=True)
    start_latitude = models.FloatField(null=True, blank=True)
    start_longitude = models.FloatField(null=True, blank=True)
    mid_latitude = models.FloatField(null=True, blank=True)
    mid_longitude = models.FloatField(null=True, blank=True)
    end_latitude = models.FloatField(null=True, blank=True)
    end_longitude = models.FloatField(null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True, upload_to="img/stage")
    image2 = models.ImageField(null=True, blank=True, upload_to="img/stage")
    image3 = models.ImageField(null=True, blank=True, upload_to="img/stage")
    image4 = models.ImageField(null=True, blank=True, upload_to="img/stage")
    image5 = models.ImageField(null=True, blank=True, upload_to="img/stage")
    image6 = models.ImageField(null=True, blank=True, upload_to="img/stage")
    image7 = models.ImageField(null=True, blank=True, upload_to="img/stage")
    image8 = models.ImageField(null=True, blank=True, upload_to="img/stage")
    gpx = models.BooleanField(null=True, blank=True, verbose_name='gpx')
    auto_gpx = models.BooleanField(null=True, blank=True, verbose_name='auto_gpx')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Stage"
        verbose_name_plural = "Stages"
        ordering = ["order"]

    def __str__(self):
        return self.title


class OpenWeatherMap(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Izena')
    owm = models.CharField(max_length=200, null=True, blank=True, verbose_name='code')
    path = models.CharField(max_length=200, null=True, blank=True, verbose_name='webpath')
    euskalmet = models.CharField(max_length=200, null=True, blank=True, verbose_name='euskalmet icon')
    euskalmet_new = models.CharField(max_length=200, null=True, blank=True, verbose_name='euskalmet icon new')
    icon = models.ImageField(null=True, blank=True, verbose_name='Icon', upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Sortze data')
    updated = models.DateTimeField(auto_now=True, verbose_name='Edizio data')

    class Meta:
        verbose_name = "OpenWeatherMap"
        verbose_name_plural = "OpenWeatherMap"
        ordering = ["created"]

    def __str__(self):
        return self.title


class Warmshower(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.CASCADE)
    town = models.CharField(max_length=200, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True, upload_to="img/warmshower")
    image2 = models.ImageField(null=True, blank=True, upload_to="img/warmshower")
    image3 = models.ImageField(null=True, blank=True, upload_to="img/warmshower")
    image4 = models.ImageField(null=True, blank=True, upload_to="img/warmshower")
    image5 = models.ImageField(null=True, blank=True, upload_to="img/warmshower")
    image6 = models.ImageField(null=True, blank=True, upload_to="img/warmshower")
    image7 = models.ImageField(null=True, blank=True, upload_to="img/warmshower")
    image8 = models.ImageField(null=True, blank=True, upload_to="img/warmshower")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Warmshower"
        verbose_name_plural = "Warmshowers"
        ordering = ["created"]

    def __str__(self):
        return self.title


class GpsTracks(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.CASCADE)
    town = models.CharField(max_length=200, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    done = models.BooleanField(null=True, blank=True)
    gpx_path = models.FileField(upload_to="gpx_path")
    gpx = models.BooleanField(null=True, blank=True, verbose_name='gpx')
    auto_gpx = models.BooleanField(null=True, blank=True, verbose_name='auto_gpx')
    color = models.CharField(max_length=100, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True, upload_to="img/gps_track")
    image2 = models.ImageField(null=True, blank=True, upload_to="img/gps_track")
    image3 = models.ImageField(null=True, blank=True, upload_to="img/gps_track")
    image4 = models.ImageField(null=True, blank=True, upload_to="img/gps_track")
    image5 = models.ImageField(null=True, blank=True, upload_to="img/gps_track")
    image6 = models.ImageField(null=True, blank=True, upload_to="img/gps_track")
    image7 = models.ImageField(null=True, blank=True, upload_to="img/gps_track")
    image8 = models.ImageField(null=True, blank=True, upload_to="img/gps_track")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "GpsTrack"
        verbose_name_plural = "GpsTracks"
        ordering = ["created"]

    def __str__(self):
        return self.title


class Icon(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    start = models.ImageField(null=True, blank=True, upload_to="img/icon")
    start_flag = models.ImageField(null=True, blank=True, upload_to="img/icon")
    end = models.ImageField(null=True, blank=True, upload_to="img/icon")
    end_flag = models.ImageField(null=True, blank=True, upload_to="img/icon")
    shadow = models.ImageField(null=True, blank=True, upload_to="img/icon")
    bike = models.ImageField(null=True, blank=True, upload_to="img/icon")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Icon"
        verbose_name_plural = "Icons"
        ordering = ["created"]

    def __str__(self):
        return self.title


class PointsInterest(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    youtube = models.CharField(max_length=500, null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True, upload_to="img/pointsInterest")
    image2 = models.ImageField(null=True, blank=True, upload_to="img/pointsInterest")
    image3 = models.ImageField(null=True, blank=True, upload_to="img/pointsInterest")
    image4 = models.ImageField(null=True, blank=True, upload_to="img/pointsInterest")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Interesting point"
        verbose_name_plural = "Points of interest"
        ordering = ["created"]

    def __str__(self):
        return self.title


class GpsTrackingData(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    date_time = models.DateTimeField(null=True, blank=True, verbose_name="fechahora")
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    track_data = models.JSONField(null=True, blank=True, verbose_name="Tracking data")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "GpsTrackingData"
        verbose_name_plural = "GpsTrackingData"
        ordering = ["created"]

    def __str__(self):
        return self.title
