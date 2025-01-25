from django.urls import path, include
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = 'restapi_app' 

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('get-data/', views.get_data),
    path('get-data/<str:username>/', views.get_data_by_username),
    path('add-data/', views.add_data),
    path('update-data/<str:username>/', views.update_data_by_username),
    path('delete-data/<str:username>/', views.delete_data_by_username),
]