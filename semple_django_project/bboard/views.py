from django.shortcuts import render

from .models import BboardPost

def index(request):
    bb_posts = BboardPost.objects.all()
    return render(request, 'bboard/index.html', {'bb_posts': bb_posts})
