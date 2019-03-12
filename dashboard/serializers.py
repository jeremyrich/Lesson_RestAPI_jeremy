from rest_framework import serializers

from account.models import Account, Students
from dashboard.models import Lesson, Status, Subscriptions
from account.serializers import StudentsAccountSerializer


# Primary serializers
class StatusSerializer(serializers.ModelSerializer):
    """ Serialiser for status model, used as nested in suscriptions serializers"""

    class Meta:
        model = Status
        fields = ("status_id", "name")


class LessonSerializer(serializers.ModelSerializer):
    """ Serialiser for Lesson model, used in LessonList view """

    class Meta:
        model = Lesson
        fields = ("lesson_id", "date", "description")


class LockLessonSerializer(serializers.ModelSerializer):
    """ Serialiser for Locked Lesson model, used in LockLesson view """

    class Meta:
        model = Lesson
        fields = ("lesson_id", "date", "description", "lock_status")
        read_only_fields = ("description", "date")


class SubscriptionsSerializer(serializers.ModelSerializer):
    """ Serializer for subscriptions model, used in SubscriptionsCreateList"""

    class Meta:
        model = Subscriptions
        fields = ("account_id",)


# Nested serializers and / or primarykeyrelatedfields
class LessonEnrollSerializer(serializers.ModelSerializer):
    """ serializer to enroll a student to a lesson using primary keys"""

    lesson_id = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Lesson.objects.all()
    )
    student_id = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Students.objects.all()
    )

    class Meta:
        model = Lesson
        fields = ("lesson_id", "student_id")

    def save(self):
        lesson = self.validated_data["lesson_id"]
        new_student = self.validated_data["student_id"]
        lesson.student_id.add(new_student)
        lesson.save()


class LessonStudentSerializer(serializers.ModelSerializer):
    """ Serializer for Lesson including students serializer """

    student_id = StudentsAccountSerializer(many=True)

    class Meta:
        model = Lesson
        fields = ("lesson_id", "date", "description", "student_id")


class SubscriptionsStatusSerializer(serializers.ModelSerializer):
    """ Subscriptions serializer including subscription_id in read_only and status as foreign key"""

    subscription_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Subscriptions
        fields = ("subscription_id", "status")


class SubscriptionsStatusNestedSerializer(serializers.ModelSerializer):
    """ Subscriptions serializer including subscription_id in read_only and status as foreign key"""

    subscription_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    status = StatusSerializer()

    class Meta:
        model = Subscriptions
        fields = ("subscription_id", "status")


class AccountSubscriptionsListSerializer(serializers.ModelSerializer):

    subscriptions = SubscriptionsStatusNestedSerializer(many=True)

    class Meta:
        model = Account
        fields = ["name", "email", "subscriptions"]


class SubscriptionsLessonSerializer(serializers.ModelSerializer):
    """  Subscriptions serializer including Lessons and status as nested fields """

    status = StatusSerializer(many=False)
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Subscriptions
        fields = ("subscription_id", "status", "subscription_date", "lessons")
