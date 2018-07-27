from django.conf.urls import url
from cafe import views
from rest_framework_jwt.views import obtain_jwt_token
from .views import CreateUserAPIView, UserRetrieveUpdateAPIView

urlpatterns = [
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^table/$', views.TableListView.as_view()),
    url(r'^table/(?P<pk>[0-9]+)/$', views.TableDetailView.as_view()),
    url(r'^role/$', views.RoleListView.as_view()),
    url(r'^role/(?P<pk>[0-9]+)/$', views.RoleDetailView.as_view()),
    url(r'^department/$', views.DepartmentListView.as_view()),
    url(r'^department/(?P<pk>[0-9]+)/$', views.DepartmentDetailView.as_view()),
    url(r'^user/$', views.UserListView.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view()),
    url(r'^mealcategory/$', views.MealCategoryListView.as_view()),
    url(r'^mealcategory/(?P<pk>[0-9]+)/$', views.MealCategoryDetailView.as_view()),
    url(r'^persentage/$', views.ServicePersentageListView.as_view()),
    url(r'^persentage/(?P<pk>[0-9]+)/$', views.ServicePersentageDetailView.as_view()),
    url(r'^meal/$', views.MealListView.as_view()),
    url(r'^meal/(?P<pk>[0-9]+)/$', views.MealDetailView.as_view()),
    url(r'^order/$', views.OrderListView.as_view()),
    url(r'^order/(?P<pk>[0-9]+)/$', views.OrderDetailView.as_view()),
    url(r'^check/$', views.CheckListView.as_view()),
    url(r'^check/(?P<pk>[0-9]+)/$', views.CheckDetailView.as_view()),
    url(r'^create/$', CreateUserAPIView.as_view()),
    url(r'^update/$', UserRetrieveUpdateAPIView.as_view()),

]