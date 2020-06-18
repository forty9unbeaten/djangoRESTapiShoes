from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=75)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style = models.CharField(max_length=75)

    def __str__(self):
        return self.style


class ShoeColor(models.Model):
    colors = [
        ('RED', 'Red'),
        ('ORG', 'Orange'),
        ('YLW', 'Yellow'),
        ('GRN', 'Green'),
        ('BLU', 'Blue'),
        ('IND', 'Indigo'),
        ('VLT', 'Violet'),
        ('BLK', 'Black'),
        ('WHT', 'White')
    ]

    color_name = models.CharField(
        max_length=3,
        choices=colors
    )

    def __str__(self):
        return self.color_name


class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=75)
    manufacturer = models.ForeignKey(
        to='Manufacturer', on_delete=models.CASCADE)
    color = models.ForeignKey(to='ShoeColor', on_delete=models.CASCADE)
    material = models.CharField(max_length=75)
    shoe_type = models.ForeignKey(to='ShoeType', on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=75)
