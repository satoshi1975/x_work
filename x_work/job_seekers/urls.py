from django.urls import path
from . import views
from x_work import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cv_list/<int:user_id>', views.cv_list),
    path('<int:user_id>/create', views.create_cv),
    path('<int:user_id>/edit', views.create_cv),
    path('CV/<int:cv_id>/', views.cv_list, name='cv_detail'),
] 