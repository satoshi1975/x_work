from django.urls import path
from . import views
from x_work import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main_page, name='main_page'), #main page
    path('set_up', views.register, name='register'), #create account
    path('log_in', views.log_in, name='login'), #log in user
    path('log_out', views.log_out, name='logout'), #log out user
    path('profile',views.profile, name='edit_profile'), #edit user profile
    path('get_city/', views.get_city), #get city for autocomplete
    path('get_occupation/', views.get_occupation), #get occupation for autocomplete
    path('profile/<int:user_id>', views.show_profile), #show employer/job seeker profile
    path('articles/<int:article_id>', views.show_articles_list), #list of articles
    # path('employer_profile/<int:user_id>', views.employer_profile),
    
    # path("chat/<int:user_id>/", views.chat_room, name="chat_room"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
