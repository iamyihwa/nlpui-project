from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', admin.site.urls),
    path('english', views.english, name = 'english' ),
    path('spanish', views.spanish, name = 'spanish' ),
    path('romanian', views.romanian, name = 'romanian' ),
    path('multilanguages', views.multilanguages, name = 'multilanguages' ),
    #path('nlpmodules/', include('nlpmodules.urls')),
]
