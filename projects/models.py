from django.db import models

class Project(models.Model):
    TOPICS = (
        ('DE', 'Data Engineering'),
        ('ML', 'Machine Learning'),
        ('BI', 'Business Intelligence'),
        ('WD', 'Web Development'),
        ('SE', 'Software Engineering'),
        ('O', 'Other'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    topic = models.CharField(max_length=2, choices=TOPICS)
    tech_stack = models.CharField(max_length=20)
    source_code = models.URLField(max_length=200)
    image = models.FilePathField(path='/img')

    def __str__(self):
        return (self.title)
