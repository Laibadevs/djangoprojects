from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/', views.blog_details, name="blog"),
    path('blog/conditions/', views.about_details, name="conditions"),
]