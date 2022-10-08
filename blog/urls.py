from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('blogview/<str:pk>/',views.blogview,name='blogview'),
]