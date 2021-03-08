from accounts.views import *
from System.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('login/home/', home_view),
    path('adding_user_to_group/<int:group_id>/', adding_user_to_group_view),
    path('adding_user_to_group/<int:group_id>/<int:user_id>/delete/', delete_user_to_group_view),
    path('adding_user_to_group/<int:group_id>/group_expenses/', group_expenses_view),
]
