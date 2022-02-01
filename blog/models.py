from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    post_description = models.CharField(max_length=280, blank=True)
    is_draft = models.BooleanField(default=True)
    created_on = models.DateTimeField('date created')
    body = models.TextField()

    def __str__(self):
        return self.title
