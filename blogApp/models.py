from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

'''
the class Post is a Django Model,
so Django knows that it should be
saved in the database
'''


class Post(models.Model):
    '''
    define the properties of each (blog) Post
    https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types
    '''
    # link to another model
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # define text with a limited number of characters.
    title = models.CharField(max_length=200)
    # long text without a limit
    text = models.TextField()
    # date and time
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    '''
    Method publish
    Saves the model
    '''

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    '''
    Method __str__
    toString() the title of the Post
    '''

    def __str__(self):
        return self.title
