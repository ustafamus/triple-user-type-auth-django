from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('service/', views.service, name='service'),
    path('c-register/', views.customer_register, name='c-register'),
    path('s-register',views.service_register, name='s-register'),
    path('logout/', views.logout_view, name='logout_view'),
]