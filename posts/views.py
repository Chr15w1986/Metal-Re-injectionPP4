"""Post Views"""
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    """ Post list views """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "posts.html"
    paginate_by = 3
