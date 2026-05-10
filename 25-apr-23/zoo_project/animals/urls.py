from django.urls import path
from . import views

app_name = 'animals'

urlpatterns = [
    path('', views.AnimalListView.as_view(), name='animal-list'),
    path('<int:pk>/', views.AnimalDetailView.as_view(), name='animal-detail'),
    path('create/', views.AnimalCreateView.as_view(), name='animal-create'),
    path('<int:pk>/update/', views.AnimalUpdateView.as_view(), name='animal-update'),
    path('<int:pk>/delete/', views.AnimalDeleteView.as_view(), name='animal-delete'),
    path('archive/', views.AnimalArchiveIndexView.as_view(), name='animal-archive-index'),
    path('archive/<int:year>/', views.AnimalYearArchiveView.as_view(), name='animal-year-archive'),
    path('account/signup/', views.SignUpView.as_view(), name='signup'),
    path('search/', views.AnimalSearchView.as_view(), name='animal-search'),
    path('today/', views.AnimalTodayArchiveView.as_view(), name='animal-today-archive'),
]