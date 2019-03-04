from rest_framework import serializers
from .models import Account, Students


class StudentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Students
        fields = ('first_name', 'last_name', 'birthday', 'email')


class AccountIdSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Account
        fields = ('name',)


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Account
        fields = ('account_id','name', 'email', 'password', 'address')

class AccountStudentSerializer(serializers.HyperlinkedModelSerializer):
    students = StudentsSerializer(many=True, read_only=True)
    
    class Meta:
        model = Account
        fields = ('name', 'email', 'address', 'students' )

