from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=20)
    pub_date = models.DateField()
    body = models.TextField()
    feedback = models.TextField()
    good_point = models.TextField()

    def __str__(self):
        return self.title