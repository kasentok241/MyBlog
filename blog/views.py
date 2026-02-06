from django.shortcuts import render
from .models import Post

def post_list(request):
    # Fetch all posts from the database
    posts = Post.objects.all()
    # Pass them to the template
    return render(request, 'post_list.html', {'posts': posts})