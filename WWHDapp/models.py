from django.db import models
# Create your models here.

class Post(models.Model):
    objects = models.Manager()
    brand = models.ForeignKey('Brand', default="",on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(default="설명 입력")
    pic = models.ImageField(upload_to = "image", blank=True)
    category = models.ForeignKey('Category', default="",on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    objects = models.Manager()
    name = models.TextField(max_length=20)
    pic = models.ImageField(upload_to = "image", blank=True)
    def __str__(self):
        return self.name

class Brand(models.Model):
    objects = models.Manager()
    name = models.TextField(max_length=20)
    category = models.ForeignKey('Category', default="",on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

