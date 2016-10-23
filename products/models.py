from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Stat(models.Model):
    category_count = models.IntegerField()
    status = models.BooleanField(default=0)

    def __str__(self):
        return str(self.category_count)


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name