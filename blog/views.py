from django.shortcuts import render, HttpResponse
from .models import Post
import datetime

def index(request):
    if request.method == 'POST':
        post_title = request.POST["post_title"]
        post_content = request.POST["post_content"]
        post_date = '{dt:%B} {dt.day}, {dt.year} {dt:%I}:{dt:%M%p}'.format(dt=datetime.datetime.now())
        Post(title=post_title, content=post_content, date=post_date).save()

    posts = Post.objects.order_by('-id')[:]
    return render(request, 'blog/index.html', {'posts': posts})
