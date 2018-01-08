from django.db import models

# Create your models here.


class Product(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    sprice = models.FloatField(default=0)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.brand


class invertory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    storeNum = models.PositiveIntegerField(default=0)
    currentStore = models.PositiveIntegerField(default=5, editable=False)
    soldNum = models.PositiveIntegerField(default=5, editable=False)


class Customer(models.Model):
    sex = ((None, ' '), ('0', 'male'), ('1', 'female'),)
    name = models.CharField(max_length=20)
    gender = models.CharField(
        max_length=20, choices=sex, blank=False)
    paymethod = models.PositiveIntegerField(default=0)
    referer = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    expdate = models.DateField('exp date')
    activedate = models.DateField('active date')
    paprice = models.FloatField(default=0)
    soldtime = models.DateField('sold time', auto_now=True)
