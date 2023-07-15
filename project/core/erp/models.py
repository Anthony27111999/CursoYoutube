from django.db import models
from datetime import datetime


class Item(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        db_table = 'tipo'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', default="")


class Employee(models.Model):
    categ = models.ManyToManyField(Category)
    type = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='Nombre', default="")
    ci = models.CharField(max_length=8, verbose_name='C.I')
    date_create = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=00.00, max_digits=2, decimal_places=2)
    state = models.BooleanField(default=True)
    geder = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatar')
    CVitae = models.FileField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']
















