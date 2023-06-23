from django.urls import path
from . import views
from x_work import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('set_up', views.register, name='register'),
    path('log_in', views.log_in, name='login'),
    path('log_out', views.log_out, name='logout'),
    path('profile',views.profile, name='edit_profile'),
    path('get_city/', views.get_city),
    path('get_occupation/', views.get_occupation),
    path('profile/<int:user_id>', views.show_profile),
    path('articles/<int:article_id>', views.show_articles_list),
    # path('employer_profile/<int:user_id>', views.employer_profile),
    
    # path("chat/<int:user_id>/", views.chat_room, name="chat_room"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
