from django.urls import path
from .views import get_user, create_user, user_requests

urlpatterns = [
    path('user/', get_user, name='get_user_data'),
    path('user/create', create_user, name='post_user_data'),
    path('user/<int:pk>', user_requests,name="pk")
]