from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('webcafe/news/', views.NewsView.as_view(), name='news'),
    path('webcafe/menu/', views.MenuView.as_view(), name='menu'),
    path('webcafe/news/create/', views.CreateNewsView.as_view(), name='news-create'),
    path('webcafe/menu/create/', views.CreateMenuView.as_view(), name='menu-create'),
    path('webcafe/news/<int:pk>/update/', views.UpdateNewsView.as_view(), name='news-update'),
    path('webcafe/menu/<int:pk>/update/', views.UpdateMenuView.as_view(), name='menu-update'),
    path('webcafe/contact/', views.contact_form, name='contact_form'),
    path('webcafe/contact/complete/', views.contact_complete, name='contact_complete'),
    # path('webcafe/accounts/', name='accounts_edit'),
]
