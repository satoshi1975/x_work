from django.urls import path
from employers import views
from x_work import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:user_id>/create_vacancy', views.create_vacancy, name='create_vacancy'), #create vacancy
    path('<int:user_id>/vacancy_list', views.vacancy_list, name='vacancy_list'), #list of vacancies
    path('show/<int:vacancy_id>/', views.show_vacancy), #show vacancy
    path('<int:vacancy_id>/edit', views.edit_vacancy, name='edit_vacancy'), #edit vacancy
    path('search/', views.CVSearchView.as_view(),name='search_cv'), #search resume
    path('reply/<int:cv_id>', views.reply_to_cv,name='reply_cv'), #reply to resume
] 