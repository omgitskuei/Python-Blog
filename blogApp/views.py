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
from .forms import PostForm
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


def post_list(request):
    allPostsWithPDate = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': allPostsWithPDate})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

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
            post.published_date = timezone.now()
            post.save()
            # go to the post_detail page for our newly created blog post
            return redirect('post_detail', pk=post.pk)
    # when we access the page for the first time, we want a blank form;
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

'''
post/<int:pk>/edit/
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
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    # if editing a post
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
