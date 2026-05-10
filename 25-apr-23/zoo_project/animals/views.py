from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, TodayArchiveView
from django.urls import reverse_lazy
from .models import Animal
from django.db.models import Q

# Create your views here.

class AnimalListView(LoginRequiredMixin, ListView):
    model = Animal
    template_name = 'animals/animal_list.html'
    context_object_name = 'animals'
    paginate_by = 25

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Animal.objects.filter(Q(name__icontains=query))
        return Animal.objects.all()
    

class AnimalDetailView(LoginRequiredMixin, DetailView):
    model = Animal
    template_name = 'animals/animal_detail.html'


class AnimalCreateView(LoginRequiredMixin, CreateView):
    model = Animal
    fields = ['name', 'age', 'weight', 'born_in_captivity', 'date_added']
    success_url = reverse_lazy('animals:animal-list')


class AnimalUpdateView(LoginRequiredMixin, UpdateView):
    model = Animal
    fields = ['name', 'age', 'weight', 'born_in_captivity', 'date_added']
    template_name = 'animals/animal_form.html'
    success_url = reverse_lazy('animals:animal-list')


class AnimalDeleteView(LoginRequiredMixin, DeleteView):
    model = Animal
    template_name = 'animals/animal_confirm_delete.html'
    success_url = reverse_lazy('animals:animal-list')


class AnimalArchiveIndexView(LoginRequiredMixin, ArchiveIndexView):
    model = Animal
    date_field = 'date_added'
    template_name = 'animals/animal_archive.html'


class AnimalYearArchiveView(LoginRequiredMixin, YearArchiveView):
    queryset = Animal.objects.all()
    date_field = 'date_added'
    make_object_list = True


class AnimalSearchView(LoginRequiredMixin, ListView):
    model = Animal
    template_name = 'animals/animal_search.html'
    context_object_name = 'animals'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Animal.objects.filter(Q(name__icontains=query))
        return Animal.objects.none()
    

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('animals:animal-list')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create Account'
        return context
    

class AnimalTodayArchiveView(LoginRequiredMixin, TodayArchiveView):
    queryset = Animal.objects.all()
    date_field = 'date_added'
    template_name = 'animals/animal_list.html'
    context_object_name = 'animals'
    allow_empty = True