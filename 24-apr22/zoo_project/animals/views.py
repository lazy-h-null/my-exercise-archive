from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView)
from .models import Animal
from .forms import AnimalSearchForm
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, TodayArchiveView
from django.views.generic import RedirectView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'animals/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Welcome to the Zoo'
        context['total_animals'] = Animal.objects.count()
        context['captive_count'] = Animal.objects.filter(born_in_captivity=True).count()
        context['wild_count'] = Animal.objects.filter(born_in_captivity=False).count()
        return context
    

class AnimalListView(ListView):
    model = Animal
    template_name = 'animals/animal_list.html'
    context_object_name = 'animals'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_count'] = Animal.objects.count()
        return context
    

class AnimalDetailView(DetailView):
    model = Animal
    template_name = 'animals/animal_detail.html'
    context_object_name = 'animal'


class AnimalCreateView(CreateView):
    model = Animal
    fields = ['name', 'age', 'weight', 'born_in_captivity']
    template_name = 'animals/animal_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_action'] = 'Create'
        return context
    

class AnimalUpdateView(UpdateView):
    model = Animal
    fields = ['name', 'age', 'weight', 'born_in_captivity']
    template_name = 'animals/animal_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_action'] = 'Update'
        return context
    

class AnimalDeleteView(DeleteView):
    model = Animal
    template_name = 'animals/animal_confirm_delete.html'
    success_url = reverse_lazy('animals:animal-list')
    

class AnimalSearchView(FormView):
    template_name = 'animals/animal_search.html'
    form_class = AnimalSearchForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method == 'GET' and self.request.GET:
            kwargs['data'] = self.request.GET
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['results'] = None
        context['search_performed'] = False
        form = context['form']
        if self.request.GET and form.is_valid():
            data = form.cleaned_data
            queryset = Animal.objects.all()
            if data.get('name'): queryset = queryset.filter(name__icontains=data['name'])
            if data.get('min_age') is not None: queryset = queryset.filter(age__gte=data['min_age'])
            context['results'] = queryset
            context['search_performed'] = True
        return context
    

class ZooRedirectView(RedirectView):
    permanent = False
    pattern_name = 'animals:home'


class AnimalArchiveIndexView(ArchiveIndexView):
    model = Animal
    date_field = 'date_added'
    template_name = 'animals/animal_archive.html'
    allow_empty = True


class AnimalYearArchiveView(YearArchiveView):
    model = Animal
    date_field = 'date_added'
    template_name = 'animals/animal_archive_year.html'
    make_object_list = True
    allow_empty = True


class AnimalMonthArchiveView(MonthArchiveView):
    model = Animal
    date_field = 'date_added'
    template_name = 'animals/animal_archive_month.html'
    month_format = '%m'
    allow_empty = True

class AnimalTodayArchiveView(TodayArchiveView):
    model = Animal
    date_field = 'date_added'
    template_name = 'animals/animal_archive_day.html'
    allow_empty = True