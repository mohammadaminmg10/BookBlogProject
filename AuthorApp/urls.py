from . import views
from django.urls import path

urlpatterns = [
    path('', views.AuthorList.as_view()),
    path('<slug:slug>/', views.AuthorView.as_view()),
]
