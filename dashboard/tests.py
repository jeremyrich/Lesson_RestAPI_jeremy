# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User

import json

from rest_framework.test import APIClient

from account.models import Account, Students
from dashboard.models import Lesson, Status, Subscriptions
from dashboard.serializers import (
    StatusSerializer,
    LessonEnrollSerializer,
    LessonSerializer,
    LockLessonSerializer,
    LessonStudentSerializer,
    SubscriptionsLessonSerializer,
    SubscriptionsSerializer,
    SubscriptionsStatusSerializer,
)


class SubscriptionsTest(TestCase):
    """ Test module for GET and POST on /dashboard/create_sub and ../update_status """

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
        self.account = Account.objects.create(
            name="Company",
            email="Company@gmail.com",
            password="Company",
            address="test street",
        )
        self.account2 = Account.objects.create(
            name="Company2",
            email="Company2@gmail.com",
            password="Company2",
            address="test2 street",
        )
        self.status = Status.objects.create(name="Active")
        self.status2 = Status.objects.create(name="Paused")
        self.subscription = Subscriptions.objects.create(
            account_id=self.account
        )  # add subscription
        self.data = {"account_id": self.account2.account_id}
        self.update = {
            "subscription_id": self.subscription.subscription_id,  # update status
            "status": self.status2.status_id,
        }

    def test_get_subscription(self):
        response = self.client.get(reverse("dashboard:dash_create_sub"), format="json")
        subscription = Subscriptions.objects.all()
        serializer = SubscriptionsSerializer(subscription, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(
            Subscriptions.objects.get(account_id=self.account).account_id,
            self.account,  # subscription found
        )
        self.assertEqual(response.status_code, 200)  # url permissions check

    def test_post_subscription(self):
        response = self.client.post(
            reverse("dashboard:dash_create_sub"), data=self.data, format="json"
        )
        subscription = Subscriptions.objects.get(account_id=self.account2)
        serializer = SubscriptionsSerializer(subscription, many=False)
        self.assertEqual(response.status_code, 201)  # relation created
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(
            Subscriptions.objects.get(
                account_id=self.account2
            ).account_id,  # object in DB
            self.account2,
        )

        self.assertEqual(
            Subscriptions.objects.get(
                subscription_id=self.subscription.subscription_id  # default status = None
            ).status,
            None,
        )
        response2 = self.client.post(
            reverse("dashboard:dash_update_status"), data=self.update, format="json"
        )
        subscription = Subscriptions.objects.get(account_id=self.account)
        serializer = SubscriptionsStatusSerializer(subscription, many=False)
        self.assertEqual(serializer.data, response2.data)
        self.assertEqual(
            Subscriptions.objects.get(
                subscription_id=self.subscription.subscription_id  # status updated
            ).status,
            self.status2,
        )


class StatusTest(TestCase):
    """ Test module for GET on /dashboard/all_status """

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
        self.status = Status.objects.create(name="Active")

    def test_get_status(self):
        response = self.client.get(reverse("dashboard:dash_status"), format="json")
        status = Status.objects.all()
        serializer = StatusSerializer(status, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(
            Status.objects.get(name=self.status), self.status  # status found
        )
        self.assertEqual(response.status_code, 200)  # url permissions check


class LessonTest(TestCase):
    """ Test module for GET and POST on /dashboard/lesson ../create_lesson and ../lock_lesson """

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="test",
            first_name="test",
            last_name="test",
            email="test@test.com",
            password="Test123456",
        )
        self.account = Account.objects.create(
            name="Company",
            email="Company@gmail.com",
            password="Company",
            address="test street",
        )
        self.student = Students.objects.create(
            first_name="first",
            last_name="last",
            birthdate="1991-03-01",
            email="test@gmail.com",
            account_id=self.account,
        )
        self.student2 = Students.objects.create(
            first_name="first2",
            last_name="last2",
            birthdate="1991-03-01",
            email="test2@gmail.com",
            account_id=self.account,
        )
        self.client.login(username="test", password="Test123456")
        self.lesson = Lesson.objects.create(
            date="2019-01-03", description="Django crash course"
        )
        self.data = {"date": "2019-02-04", "description": "soft skills"}
        self.lock = {"lock_status": True}
        self.enrol = {
            "lesson_id": self.lesson.lesson_id,
            "student_id": self.student.students_id,
        }
        self.enrol_onlock = {"lesson_id": 1, "student_id": self.student2.students_id}

    def test_get_lesson(self):
        response = self.client.get(reverse("dashboard:dash_lesson"), format="json")
        lesson = Lesson.objects.all()
        serializer = LessonStudentSerializer(lesson, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(
            Lesson.objects.get(description=self.lesson).description,
            self.lesson.description,  # lesson found
        )
        self.assertEqual(response.status_code, 200)  # url permissions check

    def test_post_put_lesson(self):
        response = self.client.post(
            reverse("dashboard:dash_create_lesson"), data=self.data, format="json"
        )
        lesson = Lesson.objects.get(lesson_id=4)
        serializer = LessonStudentSerializer(lesson, many=False)
        self.assertEqual(response.status_code, 201)  # relation created
        self.assertEqual(
            lesson.description, response.data["description"]  # object in DB
        )

        """ check lock_lesson PUT method """
        self.assertFalse(lesson.lock_status)  # default lock_status = False
        response2 = self.client.put(
            reverse("dashboard:lock_lesson", kwargs={"pk": 3}),
            data=self.lock,
            format="json",
        )
        lesson = Lesson.objects.get(pk=3)
        self.assertTrue(lesson.lock_status)  # lock_status update = True

    def test_enroll_student_lesson(self):
        response = self.client.post(
            reverse("dashboard:dash_enrol_student"), data=self.enrol, format="json"
        )
        self.assertEqual(response.status_code, 200)

        """ lock lesson and check enroll again """
        lock = self.client.put(
            reverse("dashboard:lock_lesson", kwargs={"pk": 1}),
            data=self.lock,
            format="json",
        )
        response2 = self.client.post(
            reverse("dashboard:dash_enrol_student"),
            data=self.enrol_onlock,
            format="json",
        )
        self.assertEqual(response2.status_code, 423)  # locked status code
