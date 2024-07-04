from django.urls import path
from .views import home, books

urlpatterns = [
    path('', home, name='home'),
    path('book/', books, name='book'),
]