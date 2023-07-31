from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('login_complete/', views.LoginCompleteView.as_view(), name='login_complete'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout_complete/', views.LogoutCompleteView.as_view(), name='logout_complete'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signup_complete/', views.SignupCompleteView.as_view(), name='signup_complete'),
    path('setting/', views.AccountEditView.as_view(), name='account'),
    path('rename_complete/', views.RenameCompleteView.as_view(), name='rename_complete'),
]
