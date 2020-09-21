from django.shortcuts import render

def index(request):
  context = {
    'judul': 'Web dengan Django Framwork',
    'subjudul': 'Selamat datang',
  }
  return render(request, 'index.html', context)