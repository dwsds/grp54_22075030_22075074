from django.urls import path
from . import views


app_name = 'app1'

urlpatterns = [
path('', views.index, name='index'),  # Example URL pattern
path('about/', views.about, name='about'),
path('illness-form/<int:user_age>/<int:user_height>/<int:user_weight>/<int:user_lost>/<str:user_name>/', views.illness_form, name='illness_form'),

path('login/', views.login_view, name='login'),
path('create-superuser/', views.create_superuser, name='create_superuser'),
path('home/', views.homepage, name='home'),
path('add-user-info/', views.add_user_info, name='add_user_info'),
]