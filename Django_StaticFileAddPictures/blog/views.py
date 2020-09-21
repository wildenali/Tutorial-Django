from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    'judul': 'Blog',
    'subjudul': 'Ini adalah blog page',
  }
  return render(request, 'blog/index.html', context)