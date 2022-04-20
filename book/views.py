from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from . import models


def hello_word(request):
    return HttpRequest()

def book_all(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book': book})

def book_detail(request, id):
    book = get_object_or_404(models.Book, id=id)
    return render(request, 'book_detail.html',{'book': book})