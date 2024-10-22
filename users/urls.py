from django.urls import path
from .views import create_user, update_user, delete_user, index,user_list

urlpatterns = [
    path("", index, name="index"),
    path("users/" , user_list, name="users"),
    path('create_user/', create_user, name='create_user'),  # Create (POST)
    path('user/<uuid:user_id>/update/', update_user, name='update_user'),  # Update (PUT)
    path('user/<uuid:user_id>/delete/', delete_user, name='delete_user'),  # Delete (DELETE)
]
