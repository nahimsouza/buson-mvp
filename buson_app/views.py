from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader


def index(request):
    return render(request, 'buson_app/index.html')