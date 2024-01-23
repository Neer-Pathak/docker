from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def serve_html(request):
    return HttpResponse(200)