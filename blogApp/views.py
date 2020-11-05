'''
more about Django views by reading the official documentation:
https://docs.djangoproject.com/en/2.2/topics/http/views/
'''
from django.shortcuts import render
from django.utils import timezone
# The dot before models means current directory or current application.
# Both views.py and models.py are in the same directory.
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm
from django.shortcuts import redirect

# Create your views here.

'''
created a function (def) called post_list that takes request
and will return the value it gets from calling another
function render that will render (put together) our template
blog/post_list.html.
https://tutorial.djangogirls.org/en/django_views/
'''

# The last parameter, {}, is a place in which we can add some
# things for the template to use.
# Want to read a little bit more about QuerySets in Django?
# Read: https://docs.djangoproject.com/en/2.2/ref/models/querysets/

'''
/
'''
# homepage
def post_list(request):
    allPostsWithPDate = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': allPostsWithPDate})


'''
/post/new/
'''
def post_new(request):
    # In post_edit.html, our <form> definition had the variable method="POST"?
    # All the fields from the form are now in request.POST
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # there was no author field in the PostForm
            # but author field is required
            # commit=False means that we don't want to save the Post model yet
            post = form.save(commit=False)
            post.author = request.user
            # below line commented so that new blog posts are saved without automatically setting
            # publish dates, posts without dates are called 'drafts'
            # post.published_date = timezone.now()
            post.save()
            # go to the post_detail page for our newly created blog post
            return redirect('post_detail', pk=post.pk)
    # when we access the page for the first time, we want a blank form;
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


'''
/post/<int:pk>/
'''
# view a single post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


'''
/post/<int:pk>/edit/
'''
# we pass an extra pk parameter from urls
def post_edit(request, pk):
    # get the Post model we want to edit
    post = get_object_or_404(Post, pk=pk)
    # if submitting new form
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # save w/o published_date, as draft
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    # if editing a post
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


'''
/drafts/
'''
# display list of drafts (posts with no publish date)
def post_draft_list(request):
    # query for unpublished posts, ordered by created_date
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


'''
/post/<pk>/publish/
'''
# publish a draft
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


'''
/post/<pk>/remove/
'''
# delete/remove a post
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


'''
/post/<int:pk>/comment/
'''
# adds new comment to a post
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})
