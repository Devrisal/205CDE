from django.urls import path
form . import views

urlpatterns = [
    path('/', views.home, name="home"),
]