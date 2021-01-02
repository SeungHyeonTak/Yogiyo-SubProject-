from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=24)


class Restaurant(models.Model):
    pass


class Food(models.Model):
    pass


class Option(models.Model):
    pass


class Order(models.Model):
    pass


class Payment(models.Model):
    pass
