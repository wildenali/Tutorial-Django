from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    'judul': 'About',
    'subjudul': 'Ini adalah about page',
    'banner': 'about/img/banner_about.png'
  }
  # return render(request, 'about/index.html', context)
  return render(request, 'index.html', context)