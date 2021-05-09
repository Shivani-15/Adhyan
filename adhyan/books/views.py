from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from .forms import BookForm
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'books/upload.html', context)

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class UploadBookView(LoginRequiredMixin,CreateView):
    
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book_list')
    template_name = 'books/upload_book.html'

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
