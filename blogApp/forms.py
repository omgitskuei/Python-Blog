from django import forms

from .models import Post, Comment

'''
If you need more information about Django forms,
you should read the documentation:
https://docs.djangoproject.com/en/2.2/topics/forms/
'''
class PostForm(forms.ModelForm):

    # where we tell Django which model
    # should be used to create this form (model = Post)
    class Meta:
        model = Post
        # which field(s) should end up in our form
        # want only title and text to be exposed
        # eg. created_date should be automatically set
        # when we create a post so don't expose that
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)
