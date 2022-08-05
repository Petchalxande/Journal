from django.contrib import admin
from django.urls import path, include

from environs import Env

env = Env()
env.read_env()


urlpatterns = [
    path(env("ADMIN_URL"), admin.site.urls),

    #User Management
    path('accounts/', include('accounts.urls')),

    # Third Party Apps
    path("ckeditor5/", include('django_ckeditor_5.urls')),

    # Journal
    path('', include('journal.urls'))
]
