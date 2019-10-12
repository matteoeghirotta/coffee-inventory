from django.db import models

class Inventory(models.Model):
    products = models.TextField()

    def __str__(self):
        return self.name
