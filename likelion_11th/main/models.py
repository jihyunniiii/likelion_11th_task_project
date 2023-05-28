from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    pub_date = models.DateField()
    body = models.TextField()
    feedback = models.TextField()
    good_point = models.TextField()
    image = models.ImageField(upload_to="post/", blank=True, null=True)

    def __str__(self):
        return self.title
    
    def titlesummary(self):
        return self.body[:20]