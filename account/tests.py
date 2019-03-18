# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Account, Students
from .serializers import AccountSerializer, StudentsAccountSerializer

from rest_framework.test import APIClient, APIRequestFactory


class AccountTest(TestCase):
    """ Test module for GET and POST on /account/create """

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="test",
            first_name="test",
            last_name="test",
            email="test@test.com",
            password="Test123456",
        )
        self.client.login(username="test", password="Test123456")
        Account.objects.create(
            name="Company",
            email="Company@gmail.com",
            password="Company",
            address="test street",
        )
        self.data = {
            "name": "Company2",
            "email": "Company2@gmail.com",
            "password": "Company2",
            "address": "test2 street",
        }

    def test_get_account(self):
        response = self.client.get(reverse("account:account_create"), format="json")
        account = Account.objects.all()
        serializer = AccountSerializer(account, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(Account.objects.get(name="Company").email, "Company@gmail.com")
        self.assertEqual(response.status_code, 200)

    def test_post_account(self):
        response = self.client.post(
            reverse("account:account_create"), data=self.data, format="json"
        )
        account = Account.objects.all()
        serializer = AccountSerializer(account, many=True)
        self.assertEqual(
            Account.objects.get(name="Company2").email, "Company2@gmail.com"
        )
        self.assertEqual(response.status_code, 201)
        response = self.client.post(
            reverse("account:account_create"), data=self.data, format="json"
        )
        self.assertEqual(response.status_code, 400)


class StudentTest(TestCase):
    """ Test module for GET and POST on /account/create_student """

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="test",
            first_name="test",
            last_name="test",
            email="test@test.com",
            password="Test123456",
        )
        self.client.login(username="test", password="Test123456")  # Force login
        self.account = Account.objects.create(
            name="Company",
            email="Company@gmail.com",
            password="Company",
            address="test street",
        )
        Students.objects.create(
            first_name="first",
            last_name="last",
            birthdate="1991-03-01",
            email="test@gmail.com",
            account_id=self.account,
        )
        self.data = {
            "first_name": "first2",
            "last_name": "last2",
            "birthdate": "1991-03-01",
            "email": "test2@gmail.com",
            "account_id": self.account.account_id,
        }

    def test_get_student(self):
        response = self.client.get(
            reverse("account:account_create_student"), format="json"
        )
        students = Students.objects.all()
        serializer = StudentsAccountSerializer(students, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(
            Students.objects.get(first_name="first").email, "test@gmail.com"
        )
        self.assertEqual(response.status_code, 200)  # Url found

    def test_post_student(self):
        response = self.client.post(
            reverse("account:account_create_student"), data=self.data, format="json"
        )
        students = Students.objects.get(first_name="first2")
        self.assertEqual(
            Students.objects.get(first_name="first2").email, "test2@gmail.com"
        )
        serializer = StudentsAccountSerializer(students, many=False)
        self.assertEqual(response.status_code, 201)  # 201 - student created
        self.assertEqual(response.data, serializer.data)
        response = self.client.post(
            reverse("account:account_create_student"), data=self.data, format="json"
        )
        self.assertEqual(response.status_code, 400)  # 400 - student already in DB

    def test_delete_student(self):
        self.assertEqual(Students.objects.count(), 1)
        response = self.client.delete(
            reverse("account:account_delete_student", kwargs={"pk": 1}),
            data=self.data,
            format="json",
        )
        self.assertEqual(Students.objects.count(), 0)  # Student deleted
        self.assertEqual(
            self.client.get(
                reverse("account:account_delete_student", kwargs={"pk": 1})
            ).content,
            "[]",
        )  # Second verification

    

