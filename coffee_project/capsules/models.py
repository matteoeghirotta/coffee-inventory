from django.db import models

class Capsule(models.Model):
    name = models.TextField()
    brand = models.TextField()
    machine = models.TextField()

    def __str__(self):
        return self.name
