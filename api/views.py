from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializer import ComapanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class= ComapanySerializer


    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        company=Company.objects.get(pk=pk)
        emps=Employee.objects.filter(company=company)

        emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
        return Response(emps_serializer.data)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class= EmployeeSerializer    