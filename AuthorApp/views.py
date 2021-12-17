from django.shortcuts import render
from django.views import generic
from .models import Author


# Create your views here.


class AuthorList(generic.ListView):
    queryset = Author.objects.filter(status=1).order_by('-name')
    template_name = 'authors.html'


class AuthorView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'
