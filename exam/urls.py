from django.urls import path
from exam.views import *

app_name = 'exam'

urlpatterns = [
    path('', home_page_view, name='home'),
    path('authors/', authors, name='authors'),
    path('books/', books, name='books'),
    path('members/', member, name='members'),
    path('borrowing/', borrowing, name='borrowings'),
]