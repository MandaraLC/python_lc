from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.
def hello_world(request):
    return HttpResponse(f"我是视图：{time.time()}")
