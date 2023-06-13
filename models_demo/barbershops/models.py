from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.city}, {self.address1}'


class Barbershop(models.Model):
    name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    barber = models.ManyToManyField('Barber')

    def __str__(self):
        return f'{self.name}'


class Barber(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
