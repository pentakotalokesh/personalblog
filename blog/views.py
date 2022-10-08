from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import CommentForm
def index(request):
    post = Post.objects.all()
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


    return render(request,'blog/blogview.html',context)

