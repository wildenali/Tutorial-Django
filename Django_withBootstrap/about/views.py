from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    'title': 'About',
    'heading': 'Ini About',
    'subheading': 'Ini Halaman About',
  }
  return render(request,'about/index.html', context)