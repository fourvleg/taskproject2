from django.db import models
from django.forms import ValidationError
from django.utils import timezone


class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    date = models.DateField(default=timezone.now)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"|Date: {self.date}| Category: {self.category.name}| Amount: {self.amount}| Type: {self.type.name}"

    def clean(self):
        if self.category.type != self.type:
            raise ValidationError("Категория не соответствует выбранному типу")
        if self.subcategory.category != self.category:
            raise ValidationError("Подкатегория не соответствует выбранной категории")
