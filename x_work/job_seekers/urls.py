from django.urls import path
from job_seekers import views
from x_work import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cv_list/<int:user_id>', views.cv_list),
    path('show/<int:cv_id>', views.show_cv),
    path('<int:user_id>/create_cv', views.create_cv),
    path('edit/<int:cv_id>', views.edit_cv),
    path('CV/<int:cv_id>/', views.cv_list, name='cv_detail'),
    # path('search_v/', views.search_vacancy),
    path('search/', views.VacancySearchView.as_view(), name='search_vacancy'),
] 