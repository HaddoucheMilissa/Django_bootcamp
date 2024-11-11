from django.urls import path
from .views import get_user, create_user

urlpatterns = [
    path('user/', get_user, name='get_user_data'),
    path('user/create', create_user, name='post_user_data')
]