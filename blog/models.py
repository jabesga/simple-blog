from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=10000)
    date = models.CharField(max_length=128)

    def __unicode__(self):
        return self.title