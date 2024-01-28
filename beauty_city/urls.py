from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

from salons import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", render, kwargs={"template_name": "index.html"}, name="start_page"),
    path('service/', views.service, name='service'),
    path('service_finaly/', views.service_finaly, name='service_finaly'),
    path('popup/', views.popup, name='popup'),
    path('profile/', views.profile, name='profile'),
    path('notes/', views.notes, name='notes'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('account.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT) +  \
                   static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
