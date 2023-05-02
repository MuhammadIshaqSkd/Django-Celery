from django.http import HttpResponse
from django.shortcuts import render
from .task import test_fun
# Create your views here.

def test(request):
    test_fun.delay()
    return HttpResponse("Done")