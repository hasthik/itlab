from django.contrib import admin
from django.urls import path,re_path
from home import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name=''),
    path("aboutus",views.aboutus),
    path("contact",views.contact,name='contact'),
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/', views.index, name='index')
]
