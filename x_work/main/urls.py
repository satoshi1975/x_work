from django.urls import path
from . import views
from x_work import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main_page),
    path('set_up', views.register),
    path('log_in', views.log_in),
    path('log_out', views.log_out),
    path('profile',views.profile),
    path('get_city/', views.get_city),
    path('get_occupation/', views.get_occupation),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
