from django.urls import path
from apps.main.views import index, about,contact,about_me

urlpatterns = [
    path('',index,name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('aboutme/', about_me, name='aboutme'),
]
