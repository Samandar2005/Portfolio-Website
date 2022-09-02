from django.db import models

# Create your models here.


class My(models.Model):
    name = models.CharField(max_length=250)
    bio = models.CharField(max_length=500)
    image = models.ImageField(upload_to='static/images/')

    def __str__(self):
        return f'{self.name} {self.bio} {self.image}'


class MyHistory(models.Model):
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class MyWork(models.Model):
    title = models.CharField(max_length=500)
    project_url = models.CharField(max_length=500)
    codes_url = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class MyGoals(models.Model):
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Cooperation(models.Model):
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title
