from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category, Comment
from .forms import CreateUserForm, CommentForm
from . import forms
# Create your views here.
def home(request):
    recommended_books = Book.objects.filter(recommended_books=True)
    business_books = Book.objects.filter(business_books=True)
    return render(request, 'home.html', {'recommended_books': recommended_books,
                                         'business_books': business_books})


def all_books(request):
    books = Book.objects.all()
    return render(request, 'all_books.html', {'books': books})


def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, 'genre_detail.html', {'category': category})


def book_detail(request, slug, new_comment=None):
    book = Book.objects.get(slug=slug)
    book_category = book.category.first()
    similar_books = Book.objects.filter(category__name__startswith=book_category)
    comments = book.comments.filter(active=True)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            comment_form.instance.user = request.user
            new_comment.post = book
            new_comment.save()
            return redirect('book_detail', slug=book.slug)
    else:
        comment_form = CommentForm()
    return render(request, 'book_detail.html',
                  {'book': book, 'similar_books': similar_books, 'comment_form': comment_form, 'comments': comments, 'new_comment': new_comment})


def search_book(request):
    searched_books = Book.objects.filter(title__icontains=request.POST.get('name_of_book'))
    return render(request, 'search_book.html', {'searched_books': searched_books})


def comment_create(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.post = book
            comment.author = request.user
            form.save()
            return redirect('book_detail', slug=slug)

