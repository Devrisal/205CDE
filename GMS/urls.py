
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('gymsite/', include('gsmsite.urls')),
    path('admin/', admin.site.urls),
   
    
]
