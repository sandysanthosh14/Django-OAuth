from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name='index'), 
    path('login',views.user_login, name='login'),
    path('logout',user_logout, name='logout'),
    path('users/',views.UserList.as_view()),
    path('rtoken/',views.TokenRefresh.as_view()),
]
