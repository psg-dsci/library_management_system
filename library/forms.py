from django import forms
from .models import Book, Borrow, Borrower

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn']

class BorrowForm(forms.ModelForm):
    roll_number = forms.CharField(max_length=20)
    name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = Borrow
        fields = ['book', 'roll_number', 'name', 'phone_number']
