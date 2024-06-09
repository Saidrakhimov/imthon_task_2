from django.shortcuts import render
from exam.models import *


def home_page_view(requests):
    members = Members.objects.all()
    borrowing = BorrowingRecords.objects.all()
    context = {
        'members': members,
        'borrowing': borrowing
    }
    return render(requests, 'index.html', context=context)


def authors(request):
    authors = Authors.objects.all()
    context = {
        'authors': authors,
    }
    return render(request, 'authors.html', context=context)


def books(request):
    book = Books.objects.all()
    context = {
        'books': book
    }
    return render(request,'books.html',context=context)


def member(request):
    members = Members.objects.all()
    context = {
        'members': members
    }
    return render(request,'members.html',context=context)




def borrowing(requests):
    borrowings = BorrowingRecords.objects.all()
    context = {
        'borrowings': borrowings
    }
    return render(requests,'borrowing.html', context=context)




