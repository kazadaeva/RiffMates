from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def credits(request):
    content = "Nicky\nVadim"
    return HttpReponse(content, content_tupe="text/plain")
