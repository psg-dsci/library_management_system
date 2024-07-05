from django.shortcuts import render, redirect
from .models import Book, Borrow, Borrower
from .forms import BookForm, BorrowForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

def borrow_book(request):
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            borrower, created = Borrower.objects.get_or_create(
                roll_number=form.cleaned_data['roll_number'],
                defaults={'name': form.cleaned_data['name'], 'phone_number': form.cleaned_data['phone_number']}
            )
            borrow = form.save(commit=False)
            borrow.borrower = borrower
            borrow.book.available = False
            borrow.book.save()
            borrow.save()
            return redirect('book_list')
    else:
        form = BorrowForm()
    return render(request, 'library/borrow_book.html', {'form': form})

def borrowing_history(request):
    borrows = Borrow.objects.all().order_by('-borrowed_at')
    return render(request, 'library/borrowing_history.html', {'borrows': borrows})
