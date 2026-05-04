from django.urls import path
from . import views

app_name = 'animals'

urlpatterns = [
    path('zoo/', views.ZooRedirectView.as_view(), name='zoo-redirect'),
    path('', views.HomeView.as_view(), name='home'),
    path('animals/', views.AnimalListView.as_view(), name='animal-list'),
    path('animals/<int:pk>/', views.AnimalDetailView.as_view(), name='animal-detail'),
    path('animals/add/', views.AnimalCreateView.as_view(), name='animal-create'),
    path('animals/<int:pk>/edit/', views.AnimalUpdateView.as_view(), name='animal-update'),
    path('animals/<int:pk>/delete/', views.AnimalDeleteView.as_view(), name='animal-delete'),
    path('animals/search/', views.AnimalSearchView.as_view(), name='animal-search'),
    path('animals/archive/', views.AnimalArchiveIndexView.as_view(), name='animal-archive-index'),
    path('animals/archive/<int:year>/', views.AnimalYearArchiveView.as_view(), name='animal-year-archive'),
    path('animals/archive/<int:year>/<int:month>/', views.AnimalMonthArchiveView.as_view(), name='animal-month-archive'),
    path('animals/archive/today/', views.AnimalTodayArchiveView.as_view(), name='animal-today-archive'),
]