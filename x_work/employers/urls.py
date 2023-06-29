from django.urls import path
from employers import views
from x_work import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:user_id>/create_vacancy', views.create_vacancy, name='create_vacancy'),
    path('<int:user_id>/vacancy_list', views.vacancy_list, name='vacancy_list'),
    path('show/<int:vacancy_id>/', views.show_vacancy),
    path('<int:vacancy_id>/edit', views.edit_vacancy, name='edit_vacancy'),
    path('search/', views.CVSearchView.as_view(),name='search_cv'),
] 