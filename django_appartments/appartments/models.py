from django.db import models

class Appartment(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    capacity = models.IntegerField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class Purchase(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField()
    cvv = models.CharField(max_length=50)
    iban = models.CharField(max_length=50)
    card_type = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    appartment = models.ForeignKey(Appartment, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    