from rest_framework import serializers
from cafe.models import Table, Role, Department, User, MealCategory, ServicePersentage, Meal, Order, MealToOrder, Check
from.models import User

class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = ('id', 'name')


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ('id', 'name')


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):
    role=RoleSerializer

    class Meta(object):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name',
                  'date_joined', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class MealCategorySerializer(serializers.ModelSerializer):
    department = DepartmentSerializer

    class Meta:
        model = MealCategory
        fields = ('id', 'name', 'department')


class ServicePersentageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServicePersentage
        fields = ('persentage')


class MealSerializer(serializers.ModelSerializer):
    category = MealCategorySerializer

    class Meta:
        model = Meal
        fields = ('name', 'price', 'category', 'description')


class OrderSerializer(serializers.ModelSerializer):
    waiter = RoleSerializer
    table = TableSerializer
    meal = MealSerializer(many=True)

    class Meta:
        model = Order
        fields = ('waiter', 'table', 'isitopen', 'date', 'meal')


class CheckSerializer(serializers.ModelSerializer):

    class Meta:
        model = Check
        fields = ('order', 'persentage', 'date',)

    def to_representation(self, instance):
        result = super().to_representation(instance)

        order = instance.order
        mealCounts = MealToOrder.objects.filter(order=order)
        print(mealCounts)
        total_sum = 0
        for mc in mealCounts:
            total_sum += (mc.count * mc.meal.price)
        result['total_sum'] = total_sum
        return result


