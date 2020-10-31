from django.contrib import admin
from .models import Post
'''
To learn more about Django admin, see;
https://docs.djangoproject.com/en/2.2/ref/contrib/admin/
'''
# Register your models here.
admin.site.register(Post)
