from django import forms
from .models import BookSearch, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BookSearchForm(forms.ModelForm):
    class Meta:
        model = BookSearch
        fields = ['name_of_book', ]


class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter Username'
    }))

    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter Email Address'
    }))

    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'At least eight characters'
    }))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-outline form-white',
        'placeholder': 'comment here ...',
        'rows': '5',
        'cols': '50',
    }))

    class Meta:
        model = Comment
        fields = ('body',)
