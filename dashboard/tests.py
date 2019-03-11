# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import Client, TestCase
from django.urls import reverse

from account.models import Account, Students
from dashboard.models import Lesson, Status, Subscriptions
from dashboard.serializers import (
    LessonEnrollSerializer,
    LessonSerializer,
    LessonStudentSerializer,
    SubscriptionsLessonSerializer,
    SubscriptionsSerializer,
    SubscriptionsStatusSerializer,
)


class SubscriptionsTest(TestCase):
    """ Test module for GET and POST on /dashboard/create_sub and ../update_status """

    def setUp(self):
        self.client = Client()
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
        self.subscription = Subscriptions.objects.create(account_id=self.account)
        self.data = {"account_id": self.account2.account_id}
        self.update = {
            "subscription_id": self.subscription.subscription_id,
            "status": self.status2.status_id,
        }

    def test_get_subscription(self):
        response = self.client.get(reverse("dashboard:dash_create_sub"), format="json")
        subscription = Subscriptions.objects.all()
        serializer = SubscriptionsSerializer(subscription, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(
            Subscriptions.objects.get(account_id=self.account).account_id, self.account
        )
        self.assertEqual(response.status_code, 200)

    def test_post_subscription(self):
        response = self.client.post(
            reverse("dashboard:dash_create_sub"), data=self.data, format="json"
        )
        subscription = Subscriptions.objects.get(account_id=self.account2)
        serializer = SubscriptionsSerializer(subscription, many=False)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(
            Subscriptions.objects.get(account_id=self.account2).account_id,
            self.account2,
        )

        self.assertEqual(
            Subscriptions.objects.get(
                subscription_id=self.subscription.subscription_id
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
                subscription_id=self.subscription.subscription_id
            ).status,
            self.status2,
        )
