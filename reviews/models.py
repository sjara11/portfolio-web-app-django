from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=60, default='TestUser')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    project = models.ForeignKey('projects.Project',on_delete=models.CASCADE, related_name='toaproject')

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey('Review', on_delete=models.CASCADE)
