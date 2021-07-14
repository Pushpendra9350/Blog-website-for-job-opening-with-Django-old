from django.urls import path
from . import views


urlpatterns = [
    # Why we are writing this name here as blog-home
    # it to clearify that we are talking about blog home not other apps home
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about")
]