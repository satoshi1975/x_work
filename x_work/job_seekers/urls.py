from django.urls import path
from job_seekers import views
from x_work import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cv_list/<int:user_id>', views.cv_list), #user summary list
    path('show/<int:cv_id>', views.show_cv), #show cv
    path('<int:user_id>/create_cv', views.create_cv, name='create_cv'), #create cv
    path('edit/<int:cv_id>', views.edit_cv, name='edit_cv'), #edit cv
    # path('CV/<int:cv_id>/', views.cv_list, name='cv_detail'),
    path('search/', views.VacancySearchView.as_view(), name='search_vacancy'), #search job view
    path('reply/<int:vacancy_id>', views.reply_to_vacancy, name='reply_vacancy'), #reply to vacancy
] 