from django.shortcuts import render

def index(request):
  context = {
    'title': 'Wilden Ali',
    'heading': 'Selamat Datang',
    'subheading': 'Selamat Datang di Blog Ini',
  }
  return render(request, 'index.html', context)