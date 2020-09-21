from django.http import HttpResponse

# method view
def index(request):
  judul = "<h1>Ini Home Page</h1>"
  subJudul = "<h2>Selamat datang di website ini</h2>`"
  output = judul + subJudul
  return HttpResponse(output)

def about(request):
    return HttpResponse("<h1>Ini about</h1>")