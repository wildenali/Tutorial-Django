from django.http import HttpResponse
from django.shortcuts import render

# method view
def index(request):
  return render(request, 'index.html')

def index_pageLama(request):
  judul = "<h1>Ini Home Page</h1>"
  subJudul = "<h2>Selamat datang di website ini</h2>`"
  output = judul + subJudul
  return HttpResponse(output)