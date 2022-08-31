from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

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

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


