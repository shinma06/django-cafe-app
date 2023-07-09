from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('pages/news/', views.NewsView.as_view(), name='news'),
    path('pages/menu/', views.MenuView.as_view(), name='menu'),
    path('pages/news/create/', views.CreateNewsView.as_view(), name='news-create'),
    path('pages/menu/create/', views.CreateMenuView.as_view(), name='menu-create'),
    path('pages/news/<int:pk>/update/', views.UpdateNewsView.as_view(), name='news-update'),
    path('pages/menu/<int:pk>/update/', views.UpdateMenuView.as_view(), name='menu-update'),
    path('pages/contact/', views.contact_form, name='contact_form'),
    path('pages/contact/complete/', views.contact_complete, name='contact_complete'),
]
