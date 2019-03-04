from rest_framework import serializers
from .models import Account, Students



class StudentsSerializer(serializers.ModelSerializer):
    birthday = serializers.DateField(format=None)
    class Meta:
        model = Students
        fields = ('first_name', 'last_name', 'birthday', 'email')

class StudentsAccountSerializer(serializers.ModelSerializer):
    birthday = serializers.DateField(format=None)
    class Meta:
        model = Students
        fields = ('first_name', 'last_name', 'birthday', 'email', 'account')

class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields = ('account_id', 'name', 'email', 'password', 'address')

class AccountStudentSerializer(serializers.ModelSerializer):
    students = StudentsSerializer(many=True, read_only=True)
    
    class Meta:
        model = Account
        fields = ('name', 'email', 'address', 'students' )

