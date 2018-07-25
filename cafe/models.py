from django.db import models


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


class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    dateoffadd = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'User'


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


class ServicePersentage(models.Model):
    persentage = models.IntegerField(default=0)

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
    persentage = models.ForeignKey('cafe.ServicePercentage', on_delete=models.SET_NULL, null=True)
    total_sum = models.FloatField(null=True, editable=False)

    class Meta:
        verbose_name = 'check'
        verbose_name_plural = 'checks'

    def __str__(self):
        return self.total_sum

    class Meta:
        abstract = True







