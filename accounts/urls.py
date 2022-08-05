from django.urls import include, path

from .views import UserProfileView, CustomPasswordChangeView, PasswordChangeDoneView, UpdateUserProfileView


urlpatterns = [

    path('user/', UserProfileView.as_view(), name='user'),
    path('update-profile/<str:pk>/',
         UpdateUserProfileView.as_view(), name='update-profile'),

    # Password and Account Management
    path('password/change-done/', PasswordChangeDoneView.as_view(),
         name='account_change_password_done'),
    path('password/change/', CustomPasswordChangeView.as_view(),
         name='account_change_password'),
    path('', include('allauth.urls')),
]
