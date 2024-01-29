from django.shortcuts import render, HttpResponse
from .models import Emp
from .serializers import EmpSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to the Django Project!</h1>")

@api_view(['GET','POST'])
def employeeview(request):
    if request.method == 'GET':
        my_emp = Emp.objects.all()
        ser_emp = EmpSerializer(my_emp,many=True)
        if Emp.objects.all() is None:
            return Response(serializer.data,status = status.HTTP_200_OK)
        else:
            return Response(ser_emp.data)
    elif request.method == 'POST':
        serializer = EmpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)