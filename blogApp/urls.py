'''
more about Django URLconfs,
look at the official documentation:
https://docs.djangoproject.com/en/2.2/topics/http/urls/
'''
# we're importing Django's function path and all of our views from the blogApp
from django.urls import path
from . import views

urlpatterns = [
    # assigning a view called post_list to the root URL
    # URL pattern is '' empty so resolver will match ./ homepage
    # name='post_list', is the name of the URL used to identify the view
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
