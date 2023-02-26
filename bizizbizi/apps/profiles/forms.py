
from apps.core.models import BikeSpot
from django.forms import ModelForm


class CreateSpotForm(ModelForm):
    class Meta:
        model = BikeSpot
        fields = ['title', 'country', 'town', 'description']



