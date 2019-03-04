from rest_framework import serializers
from dashboard.models import Status, Subscriptions, Lesson
from account.serializers import StudentsSerializer

class LessonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lesson
        fields = ('lesson_id', 'date', 'description')

class LessonStudentSerializer(serializers.ModelSerializer):
    students = StudentsSerializer(many=True, read_only=True)
    class Meta:
        model = Lesson
        fields = ('lesson_id', 'date', 'description', 'students')


class SubscriptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriptions
        fields = ('account',)


class SubscriptionsStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriptions
        fields = ('account', 'status')


class SubscriptionsLessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('subscription_id', 'status', 'subscription_date', 'lesson')



