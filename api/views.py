from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CompanySerializer,EmployeeSerializer
from .models import Company,Employee
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    
    #companies/{companyid}/employees
    @action(detail=True , methods=['get'])
    def employees(self,request,pk=None):
        try:
            company=Company.objects.get(pk=pk)
            employees=Employee.objects.filter(company=company)
            emp_serializer=EmployeeSerializer(employees,many=True,context={'request':request})
            return Response(emp_serializer.data)
        except Company.DoesNotExist:
            return Response({'error':'Company not found'},status=404)



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
