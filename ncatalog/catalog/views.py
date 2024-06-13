from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def home(request):
    books = Books.objects.all()
    return render(request, 'catalog/home.html', {'books': books})

def index(request):
    books = Books.objects.all()
    return render(request, 'catalog/index.html', {'books': books})

@login_required
def home(request):
    books = Books.objects.all()
    return render(request, 'catalog/home.html', {'books': books})

@login_required
def like_books(request, books_id):
    books = get_object_or_404(Books, id=books_id)
    like, created = Like.objects.get_or_create(user=request.user, books=books)
    if not created:
        like.delete()
    return redirect('detail_books', books_id=books_id)

@login_required
def comment_books(request, books_id):
    books = get_object_or_404(Books, id=books_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(user=request.user, books=books, content=content)
    return redirect('detail_books', books_id=books_id)

@login_required
def detail_books(request, books_id):
    books = get_object_or_404(Books, id=books_id)
    comments = Comment.objects.filter(books=books)
    liked = False
    if request.user.is_authenticated:
        liked = Like.objects.filter(user=request.user, books=books).exists()
    return render(request, 'catalog/detail_books.html', {'books': books, 'comments': comments, 'liked': liked})

@login_required
def add_books(request):
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Roupa cadastrada com sucesso!')
            return redirect('home')
    else:
        form = BooksForm()
    return render(request, 'catalog/add_books.html', {'form': form})

@login_required
def edit_books(request, books_id):
    books = get_object_or_404(Books, id=books_id)
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES, instance=books)
        if form.is_valid():
            form.save()
            messages.success(request, 'Roupa editada com sucesso!')
            return redirect('home')
    else:
        form = BooksForm(instance=books)
    return render(request, 'catalog/edit_books.html', {'form': form})

@login_required
def delete_books(request, books_id):
    books = get_object_or_404(Books, id=books_id)
    if request.method == 'POST':
        books.delete()
        messages.success(request, 'Roupa deletada com sucesso!')
        return redirect('home')
    return render(request, 'catalog/delete_books.html', {'books': books})