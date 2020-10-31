'''
more about Django views by reading the official documentation:
https://docs.djangoproject.com/en/2.2/topics/http/views/
'''
from django.shortcuts import render

# Create your views here.

'''
created a function (def) called post_list that takes request
and will return the value it gets from calling another
function render that will render (put together) our template
blog/post_list.html.
https://tutorial.djangogirls.org/en/django_views/
'''


def post_list(request):
    return render(request, 'blog/post_list.html', {})
