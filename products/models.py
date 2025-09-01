from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subs', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)



    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ManyToManyField(Category, blank=True, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    size = models.ManyToManyField(Size, related_name='products', blank=True, null=True)
    color = models.ManyToManyField(Color, related_name='products')

    def __str__(self):
        return self.title



