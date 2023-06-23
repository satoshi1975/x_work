from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('CV/', include('job_seekers.urls')),
    path('JOB/', include('employers.urls')),
    path('chat/', include('chat.urls')),
    # path('chat/', include('chat.routing')),
    # path('accounts/', include('django.contrib.auth.urls')),
]
