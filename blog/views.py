from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import CommentForm
def index(request):
    post = Post.objects.order_by('-date')[0:3]
    context={'post':post}
    return render(request,'blog/index.html',context)
def blogview(request,pk):
    p = Post.objects.get(id=pk)
    comments = p.comments.filter(post = p)
    new_comment = None
    count = p.comments.filter(post = p).count()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.post = p
            new_comment.id = count
            new_comment.save()
    else:
        comment_form = CommentForm()
    context={'post':p,'comment_form':comment_form,'comments':comments}

    return render(request,'blog/post.html',context)
def allposts(request):
    posts = Post.objects.all().order_by('-date')[0:10]
    context={'post':posts}
    return render(request,'blog/allposts.html',context)
