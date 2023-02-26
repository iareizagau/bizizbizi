from django.shortcuts import render

from django.views.generic.detail import DetailView
from .models import BikeSpot, OpenWeatherMap, GpsTracks, GpsTrackingData
from .models import Icon
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GpsTrackinSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


def index(request):
    bikespot = BikeSpot.objects.all().order_by("order")
    owms = OpenWeatherMap.objects.all()
    icon = Icon.objects.all()
    return render(request, "core/map.html", {'bikespot': bikespot,
                                             'owms': owms,
                                             'icon': icon})


def travels(request):
    biketravel = GpsTracks.objects.all()
    icon = Icon.objects.all()
    return render(request, "core/travel.html", {'biketravel': biketravel,
                                                'icon': icon})


# Create your views here.
class PostDetailView(DetailView):
    model = BikeSpot
    template_name = "core/detail_view.html"

    def get_context_data(self, **kwargs):
        name = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['biketravel'] = BikeSpot.objects.get(id=name)
        print(context)
        return context


class TravelDetailView(DetailView):
    model = GpsTracks
    template_name = "core/detail_view.html"

    def get_context_data(self, **kwargs):
        name = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['biketravel'] = GpsTracks.objects.get(id=name)
        print(context)
        # context['icon'] = Icon.objects.get(id=name)
        print(context)
        return context


# @api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
class GpsTrackingApiView(ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = GpsTrackinSerializer

    def get_queryset(self):
        return GpsTrackingData.objects.all()


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def GpsTrackingView(request):
    if request.method == 'POST':
        serializer = GpsTrackinSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def realtime(request):
    return render(request, "core/realTime.html")


class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)