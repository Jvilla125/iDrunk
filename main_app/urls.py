from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('userdrinks', views.userdrinks, name='userdrinks'),
    path('accounts/signup', views.signup, name='signup'),
    path('drinks/<int:drink_id>', views.drinks_detail, name='detail'),
    path('drinks/create/', views.DrinkCreate.as_view(),  name='drinks_create'),
    path('drinks/<int:pk>/update/', views.DrinkUpdate.as_view(), name='drinks_update'),
    path('drinks/<int:pk>/delete/', views.DrinkDelete.as_view(), name='drinks_delete'),
    path('fav/<int:id>', views.fav_add, name='fav_add'),
    path('drinks/favorites', views.fav_drinks, name='fav_drinks'),
    path('drinks/<int:drink_id>/add_photo/', views.add_photo, name='add_photo'),
    path('drinks/<int:drink_id>/delete_photo/', views.PhotoDelete.as_view(), name='delete_photo'),
    path('drinks/<int:drink_id>/add_review/', views.add_review, name='add_review'),
]
