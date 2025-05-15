from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def credits(request):
    content = "Nicky\nElena"
    return HttpResponse(content, content_type="text/plain")

def news(request):
    data = {"news": [
        "ReffMates now has a news page!",
        "ReffMates has its first page"
    ]}
    return render(request, "news.html", data)
