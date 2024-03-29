from rest_framework import serializers

from .models import Account, Students


# Primary serializers
class AccountSerializer(serializers.ModelSerializer):
    """ Serializer for account model """

    class Meta:
        model = Account
        fields = ("account_id", "name", "email", "password", "address")


class StudentsAccountSerializer(serializers.ModelSerializer):
    """ Serializer for Student using account as foreign key field """

    birthdate = serializers.DateField(format=None)

    class Meta:
        model = Students
        fields = ("first_name", "last_name", "birthdate", "email", "account_id")
        extra_kwargs = {"account_id": {"write_only": True}}


# Nested serializers
class AccountStudentSerializer(serializers.ModelSerializer):
    """ Serializer for account using students as nested fields """

    students = StudentsAccountSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ("name", "email", "address", "students")
