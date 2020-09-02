
from django.db import models

class Person(models.Model):
    name = models.TextField()
    surname = models.TextField()
    job = models.TextField()
    address = models.TextField()
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name

