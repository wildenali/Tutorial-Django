from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    'judul': 'Blog',
    'subjudul': 'Ini adalah blog page',
    'banner': 'blog/img/banner_blog.png'
  }
  # return render(request, 'blog/index.html', context)
  return render(request, 'index.html', context)