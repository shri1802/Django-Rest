from rest_framework import serializers
from .models import Emp

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = ['emp_id','emp_name','emp_age']