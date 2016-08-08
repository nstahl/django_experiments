from django.shortcuts import render
from django.http import HttpResponse
import pdb


def index(request):
    pdb.set_trace()
    return HttpResponse("Hello, world. You're at the polls index.")