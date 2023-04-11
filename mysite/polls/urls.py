from django.contrib import admin
from django.urls import include, path

from . import views


urlpatterns = [
    path('', include('polls.urls')),
    # path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]