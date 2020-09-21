from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  context = {
    'judul': 'Wadidaw Blog Qita',
    'pengetik': 'Mang Oleh'
  }
  # return render(request, 'blog/index.html', context)
  return render(request, 'index.html', context)

def recent(request):
  return HttpResponse('<h1>Ini adalah recent post</h1>')