from django.shortcuts import get_object_or_404, render
from datetime import date

from blog.models import Post
# Create your views here.


def get_date(post):
    return post['date']


def index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    # sorted_posts= sorted(all_posts,key=get_date)
    # latest_posts=sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        "posts": latest_posts
    })


def post(request):
    return render(request, 'blog/posts.html', {
        "all_posts": Post.objects.all().order_by("-date")
    })


def slug(request, slug):
    # identified_post=next(post for post in all_posts if post['slug']==slug)
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-details.html', {
        "post": identified_post,
        "post_tags": identified_post.tag.all()
    })
