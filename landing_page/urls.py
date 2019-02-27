from django.urls import path
from . import views

urlpatterns = [
    path('login', views.log_in, name='login'),
    path('logout', views.logout_view, name='logout'),
    # This image url, it view and the template arent working yet!
    path('images/<int:id>', views.display_image, name='images'),
    path('signup', views.register, name='sign_up'),
    path('gallery', views.gallery, name='gallery'),
    path('super/', views.super_user, name='super_user'),
    path('profile/<int:id>', views.profile, name='profile')
]
