from django.db import models

class Product(models.Model):
    article = models.TextField()
    category = models.TextField()
    capsule_system = models.ForeignKey(
        'capsules.Capsule',
        on_delete = models.CASCADE,
    )
    stock_qty = models.IntegerField()
    unit_price = models.DecimalField(max_digits=19, decimal_places=10)
    short_description = models.TextField()
    long_description = models.TextField()
    main_image = models.FileField()
    manufacturer = models.TextField()
    ean = models.TextField()
    weight = models.FloatField()
    weight_measure = models.CharField(max_length=2)
    flavour = models.TextField()

    def __str__(self):
        return self.name
