from django.contrib import admin

from .models import *

admin.site.register([
    Table, Role, Department, User, MealCategory, Meal, ServicePersentage,
])

class MealInline(admin.StackedInline):
    model = MealToOrder
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    inlines = [MealInline, ]

admin.site.register(Order, OrderAdmin)
admin.site.register(Check)