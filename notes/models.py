from django.db import models

# Create your models here.


class App(models.Model):
    name = models.TextField(max_length=100)
    url = models.URLField(max_length=200)
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.name


class Link(models.Model):
    name = models.TextField(max_length=100)
    url = models.URLField(max_length=200)
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.TextField(max_length=100)
    url = models.URLField(max_length=200)
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.name


class Guide(models.Model):
    name = models.TextField(max_length=100)
    url = models.URLField(max_length=200)
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.name
