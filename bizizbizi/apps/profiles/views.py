from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import FormView
from apps.registration.models import Profile
from .forms import CreateSpotForm
# from .models import ClimbingSpot as C2, OpenWeatherMap
# from core.models import ClimbingSpot
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404
from django.db.models import Q
from apps.core.settings import ApiKeys, Map


# Create your views here.
class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    paginate_by = 6

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        condition_1 = Q(public=True)
        condition_2 = Q(id=2)
        print(self.request.user)
        if 'admin' == str(self.request.user):
            return qs
        else:
            print("***")
            return qs.filter(public=True)


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        # context['climbingspot'] = ClimbingSpot.objects.filter(user=context['profile'])
        return context


@method_decorator(login_required, name='dispatch')
class ProfileCreateSpotFormView(FormView):
    template_name = "profiles/profile_create_spot.html"
    form_class = CreateSpotForm
    success_url = '/profiles/map'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])

    def get_context_data(self, **kwargs):
        context = super(ProfileCreateSpotFormView, self).get_context_data(**kwargs)
        try:
            context['api'] = ApiKeys
            context['map'] = Map
            return context
        except Exception as e:
            raise Http404("Given query not found....")


def test(request):
    # climbingspot = ClimbingSpot.objects.all()
    # owms = OpenWeatherMap.objects.all()
    return render(request, "profiles/test.html")


class PostDetailView(DetailView):
    # model = ClimbingSpot
    template_name = "profiles/detail_view.html"

    def get_context_data(self, **kwargs):
        name = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        # context['climbingspot'] = ClimbingSpot.objects.get(id=name)
        return context


@method_decorator(login_required, name='dispatch')
class EditPostDetailView(FormView):
    # model = ClimbingSpot
    template_name = "profiles/edit_detail_view.html"
    form_class = CreateSpotForm
    success_url = '/accounts/profiles/'
    reverse_lazy('home')

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        try:
            profiles = Profile.objects.filter(public=True)
            profiles_user = profiles.get(user=self.request.user.id)
            # context['climbingspot'] = ClimbingSpot.objects.filter(user=profiles_user).get(id=pk)
            context['api'] = ApiKeys
            context['pk'] = pk
            return context
        except Exception as e:
            raise Http404("Given query not found....")

    def form_valid(self, form, **kwargs):
        context = self.get_context_data()
        pk = int(context['pk'])

        return super(EditPostDetailView, self).form_valid(form)
