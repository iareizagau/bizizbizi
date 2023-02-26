from rest_framework import serializers
from .models import GpsTrackingData


class GpsTrackinSerializer(serializers.ModelSerializer):
    class Meta:
        model = GpsTrackingData
        fields = ('title', 'date_time', 'latitude', 'longitude', 'track_data',)
