from django.urls import path
from . import views


app_name = 'login_app'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('password_reset_request/', views.password_reset_request, name='password_reset_request'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('delete_account/', views.delete_account, name='delete_account'),
]
