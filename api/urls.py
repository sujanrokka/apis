
from django.contrib import admin
from django.urls import path,include
from .views import CompanyViewSet,EmployeeViewSet
from rest_framework import routers


router=routers.DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='companies')
router.register(r'employees', EmployeeViewSet, basename='employees')
urlpatterns = [
    path('',include(router.urls)),
]
  
