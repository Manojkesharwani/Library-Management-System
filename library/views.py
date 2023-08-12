from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book
from .models import Member
from .models import Transaction
from .forms import bookform
from .forms import Memberform
from .forms import Transactionform
import requests
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def indexx(request):
    return render(request, 'index.html')

def import_books(reqeust):
    response = requests.get('https://frappe.io/api/method/frappe-library?page=1&title=and')
    books = response.json()['message']
    print(books)
    # for num_pages in books[:20]:
    for book in books[:20]:
        book_id = book['bookID']
        title = book['title']
        authors = book['authors']
        isbn = book['isbn']
        publisher = book['publisher']
        page_count = book['  num_pages']

        Book.objects.create(
            book_id=book_id,
            title=title,
            authors=authors,
            isbn=isbn,
            publisher=publisher,
            page_count=page_count,
        )
    return redirect('home')

def book_list(request):
    books = Book.objects.filter(visibility=True)
    context = {
        "books": books
    }
    return render(request, 'book_list.html', context)

def membersview(request):
    members = Member.objects.all()
    context = {
        "members": members
    }
    return render(request, 'membersdetail.html', context)

def transactionlistview(request):
    yy = Transaction.objects.all()
    context = {
        "xx": yy
    }
    return render(request, 'transactiondetail.html', context)

class Addbook(SuccessMessageMixin, CreateView):
    model = Book
    form_class = bookform
    template_name = "bookform.html"
    # success_message = 'Appointment has been successfuly !!'
    success_url = reverse_lazy('book-list')
    
class Memberview(SuccessMessageMixin, CreateView):
    model = Member
    form_class = Memberform
    template_name = "member.html"
    # success_message = 'Appointment has been successfuly !!'
    success_url = reverse_lazy('memberlist')
    
class Transactionview(SuccessMessageMixin, CreateView):
    model = Transaction
    form_class = Transactionform
    template_name = "transaction.html"
    
    def post(self, request):
        form = self.form_class(request.POST)
        if(form.is_valid()):
            # print(form.cleaned_data['book'])
            book = Book.objects.get(id=form.cleaned_data['book'].id)
            book.visibility = False
            book.save()
            form.save()
            return redirect('transactionlist')
            
    # success_message = 'Transaction has been successfuly !!'
    success_url = reverse_lazy('transactionlist')
   
def post_delete(request, id):
    data = get_object_or_404(Book, id=id)
    data.delete()
    return redirect('home')

def edit_data(request, id):
    post_data = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form_data = bookform(request.POST, instance=post_data)
        if form_data.is_valid():
            form_data.save()
            return redirect('home')
    else:
        form_data = bookform(instance=post_data)
        myinfo = {"form_data": form_data}
    return render(request, 'bookformedit.html', context=myinfo)


class BlogSearchView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('q')
        print(query)
        return Book.objects.filter(title__icontains=query) | Book.objects.filter(authors__icontains=query)