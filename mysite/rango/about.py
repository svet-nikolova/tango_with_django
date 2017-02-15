
from django.shortcuts import render

from django.http import HttpResponse

def about(request):

    return render(request, 'rango/about.html')
