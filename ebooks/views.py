from django.shortcuts import render, redirect, get_object_or_404
from .models import  myBooks
from .forms import MyBooksForm

# Create your views here.
def home(request):
    books=myBooks.objects.all()
    context={'books':books}
    return render (request, 'index.html', context)

def add_book(request):
    form = MyBooksForm()  # Create form instance
    print(form)  # Debug: Print form in terminal to check if it’s created properly

    if request.method == "POST":
        form = MyBooksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_success')

    return render (request, 'add_book.html', {'form': form})

def delete_book(request, book_id):
    book = get_object_or_404(myBooks, id=book_id)  # Get book or return 404
    book.delete()  # Delete the book
    return redirect('home')  # Redirect back to the list page


def update_book(request, book_id):
    book = get_object_or_404(myBooks, id=book_id)  # Get book or return 404

    if request.method == "POST":
        form = MyBooksForm(request.POST, instance=book)  # Pre-fill with existing data
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect back to book list
    else:
        form = MyBooksForm(instance=book)  # Pre-fill the form for GET request

    return render(request, 'update_book.html', {'form': form, 'book': book})