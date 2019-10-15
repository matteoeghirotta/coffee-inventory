from django.db import models
from django.urls import reverse

class Product(models.Model):
    article = models.CharField(max_length=56)
    category = models.CharField(max_length=56)
    capsule_system = models.ForeignKey(
        'capsules.Capsule',
        on_delete = models.CASCADE
    )
    stock_qty = models.IntegerField()
    unit_price = models.DecimalField(max_digits=19, decimal_places=10)
    short_description = models.CharField(max_length=56)
    long_description = models.TextField()
    main_image = models.FileField()
    manufacturer = models.CharField(max_length=56)
    ean = models.CharField(max_length=56)
    weight = models.FloatField()
    weight_measure = models.CharField(max_length=2)
    flavour = models.CharField(max_length=56)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])
