from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from .managers import UserManager


class Table(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'table'
        verbose_name_plural = 'tables'

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'role'
        verbose_name_plural = 'roles'

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'department'
        verbose_name_plural = 'departments'

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self


class MealCategory(models.Model):
    Pervoe = 1
    Vtoroe = 2
    Deserts = 3
    category = (
        (Pervoe, 'Pervoe'),
        (Vtoroe, 'Vtoroe'),
        (Deserts, 'Deserts'),
    )
    name = models.IntegerField(choices=category)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'mealcategory'
        verbose_name_plural = 'mealcategories'

    def __str__(self):
        return self.name


class ServicePersentage (models.Model):
    persentage = models.IntegerField()

    class Meta:
        verbose_name = 'persentage'
        verbose_name_plural = 'persentages'

    def __str__(self):
        return self.persentage


class Meal(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(blank=True)
    category = models.ForeignKey('MealCategory', on_delete=models.CASCADE)
    description = models.CharField(max_length=60, blank=True)

    class Meta:
        verbose_name = 'meal'
        verbose_name_plural = 'meals'

    def __str__(self):
        return self.name


class Order(models.Model):
    waiter = models.ForeignKey('Role', on_delete=models.CASCADE)
    table = models.ForeignKey('Table', on_delete=models.CASCADE)
    isitopen = models.BooleanField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    meal = models.ManyToManyField(Meal, through='MealToOrder')

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        return self.waiter + ' ' + self.table


class MealToOrder(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    meal = models.ForeignKey('Meal', on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'mealtoorder'
        verbose_name_plural = 'mealstoorder'

    def __str__(self):
        return self.order + ' ' + self.meal


class Check(models.Model):
    waiter = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    persentage = models.ForeignKey(ServicePersentage, on_delete=models.SET_NULL, null=True)
    total_sum = models.FloatField(null=True, editable=False)

    class Meta:
        verbose_name = 'check'
        verbose_name_plural = 'checks'

    def __str__(self):
        return self.order







