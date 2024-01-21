from django.urls import path
from .views import index, contact, about, work_detail

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('work/<slug:slug>/', work_detail, name='work_detail'),
    path('contact/', contact, name='contact'),
]