from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def hello_view(request, *args, **kwargs):
    return render(request, "hello.html", {})

def contact_view(request, *args, **kwargs):
    my_context = {
        "my_text": "this is my_text",
        "my_number": 123,
        "my_list": [123, 4567, 5555]
    }
    return render(request, "contact.html", my_context)

def response_view(request, *args, **kwargs):
    return render(request, "response.html", {})

def order_view(request, *args, **kwargs):
    return render(request, "order.html", {})