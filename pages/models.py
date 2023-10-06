from django.db import models

class MainContent(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    pub_date=models.DateTimeField('date published')

class Necklace(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='necklaces/')
class Earring(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='earrings/')

class Let(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='lets/')