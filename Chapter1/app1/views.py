from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post

# import json

# Create your views here.
# def post_list(request):
#     posts = Post.published.all()
#     return render(request,
#     'app1/post/list.html',
#     {'posts': posts})

# def post_list(request):
#     object_list = Post.published.all()
#     paginator = Paginator(object_list, 3)
#     # print(json.dumps(request.GET))
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
    
#     return render(request, 'app1/post/list.html', {'page': page, 'posts': posts})

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'app1/post/list.html'

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug = post, status = 'published',
                                publish__year = year, 
                                publish__month = month, 
                                publish__day = day)
    return render(request, 
                'app1/post/detail.html'
                ,{'post':post})

