from django.db import models
# Create your models here.


class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title1 = models.CharField(max_length=200)
    content1 = models.TextField()
    note = models.TextField()
    title2 = models.CharField(max_length=200)
    content2 = models.TextField()
    slug = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    time = models.DateField(auto_now_add=True)
    tags1 = models.CharField(max_length=50)
    tags2 = models.CharField(max_length=50)

    def __str__(self):
        return self.title1 + " ~ " + self.title2