from django.db import models

from django.contrib.auth.models import User


class MainContent(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    pub_date=models.DateTimeField('date published')

class Necklace(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='necklaces/', blank=True)
class Earring(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='earrings/',blank=True)

class Let(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='lets/',blank=True)



class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_list = models.ForeignKey(Necklace, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.author.username

    def __str__(self):
        return self.title

class Comment2(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_list = models.ForeignKey(Earring, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.author.username

class Comment3(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_list = models.ForeignKey(Let, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.author.username