from django.db import models

# Create your models here

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)


    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='tasks', null = True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title