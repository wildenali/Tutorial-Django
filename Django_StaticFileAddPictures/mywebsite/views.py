from django.shortcuts import render

def index(request):
  context = {
    'judul': 'Web dengan Django Framwork',
    'subjudul': 'Selamat datang',
    'banner': 'img/banner_home.png'
  }
  return render(request, 'index.html', context)