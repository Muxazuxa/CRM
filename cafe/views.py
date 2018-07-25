from rest_framework import generics
from cafe.models import Table, Role, Department, User, MealCategory, ServicePersentage, Meal, Order, MealToOrder, Check
from cafe.serializers import TableSerializer, RoleSerializer, DepartmentSerializer, UserSerializer, MealCategorySerializer, ServicePersentageSerializer, MealSerializer, OrderSerializer, CheckSerializer


class TableListView(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class RoleListView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class DepartmentListView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MealCategoryListView(generics.ListCreateAPIView):
    queryset = MealCategory.objects.all()
    serializer_class = MealCategorySerializer


class MealCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MealCategory.objects.all()
    serializer_class = MealCategorySerializer


class ServicePersentageListView(generics.ListCreateAPIView):
    queryset = ServicePersentage.objects.all()
    serializer_class = ServicePersentageSerializer


class ServicePersentageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServicePersentage.objects.all()
    serializer_class = ServicePersentageSerializer


class MealListView(generics.ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class MealDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


#class CheckListView(generics.ListCreateAPIView):
  #  queryset = Check.objects.all()
   # serializer_class = CheckSerializer


#class CheckDetailView(generics.RetrieveUpdateDestroyAPIView):
   # queryset = Check.objects.all()
    #serializer_class = CheckSerializer