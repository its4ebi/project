from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # مسیر صفحه اصلی
    path('articles/', views.article_list, name='article_list'),  # مسیر لیست مقالات
    path('article/<int:id>/', views.article_detail, name='article_detail'),  # جزئیات مقالات
    path('about/', views.about, name='about'),   # مسیر برای صفحه درباره ما
    path('contact/', views.contact, name='contact'),
]

from django.urls import path
from . import views



   
