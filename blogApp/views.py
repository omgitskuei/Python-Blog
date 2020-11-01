'''
more about Django views by reading the official documentation:
https://docs.djangoproject.com/en/2.2/topics/http/views/
'''
from django.shortcuts import render
from django.utils import timezone
# The dot before models means current directory or current application.
# Both views.py and models.py are in the same directory.
from .models import Post

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
