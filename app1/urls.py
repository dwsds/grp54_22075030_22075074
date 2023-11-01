from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
path('', views.index, name='index'),  # Example URL pattern
path('about/', views.about, name='about'),
path('illness-form/', views.illness_form, name='illness_form'),
path('login/', views.login_view, name='login'),
path('signup/', views.signup, name='signup'),
]