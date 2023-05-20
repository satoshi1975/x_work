from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('set_up', views.register),
    path('log_in', views.log_in),
    path('log_out', views.log_out),
    path('profile',views.profile),
    path('geoform',views.geoform),

]
