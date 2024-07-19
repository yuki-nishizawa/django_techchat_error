from django.urls import path, include
from . import views


app_name = 'questions'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('questions/create/', views.CreateView.as_view(), name='create'),
    path('questions/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('questions/<int:pk>/answers/', include('answers.urls')),
    path('questions/<int:pk>/delete', views.DeleteView.as_view(), name='delete'),
]