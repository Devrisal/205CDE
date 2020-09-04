from django.urls import path
from  .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('navbar', views.navbar, name="navbar"),
    path('addevent', views.addevent, name="addevent"),
    path('viewuser', views.viewuser, name="viewuser"),
    path('addpackage', views.addpackage, name="addpackage"),
    path('editevent', views.editevent, name="editevent"),
    path('delete/<int:id>', views.delete), 
    path('editpackage/<int:id>', views.editpackage),
    path('update/<int:id>', views.updatepackage),
    path('deletepackage/<int:id>', views.deletepackage),
    path('cousel', views.cousel, name="cousel"),
    path('advice', views.advice, name="advice"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('viewpackages', views.viewpackages, name="viewpackages"),
    path('gallery', views.gallery, name="gallery"),
    path('fitnessclass', views.fitnessclass, name="fitnessclass")
]