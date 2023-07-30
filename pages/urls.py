from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('news/create/', views.CreateNewsView.as_view(), name='news-create'),
    path('menu/create/', views.CreateMenuView.as_view(), name='menu-create'),
    path('news/<int:pk>/update/', views.UpdateNewsView.as_view(), name='news-update'),
    path('menu/<int:pk>/update/', views.UpdateMenuView.as_view(), name='menu-update'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact_complete/', views.ContactCompleteView.as_view(), name='contact_complete'),
]
