from django.shortcuts import render
from models import News
from models import Comment
import explore
from forms import CommentForm
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def index(request):
	qs = News.objects.all()
	return render(request, 'news/posts.html',{'items': qs})

def post_detail(request,pk):
	qs = News.objects.filter(id=pk)
	return render(request, 'news/post_detail.html', {'posts': qs})

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, '/news/add_comment_to_post.html', {'form': form})
