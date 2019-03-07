from rest_framework import serializers
from dashboard.models import Status, Subscriptions, Lesson
from account.serializers import StudentsSerializer

class StatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Status
        fields = ('status_id', 'name', 'insert_date')

class LessonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lesson
        fields = ('lesson_id', 'date', 'description')

class LessonEnrollSerializer(serializers.ModelSerializer):
    lesson_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Lesson.objects.all())

    class Meta:
        model = Lesson
        fields = ('students', 'lesson_id')

    

class LessonStudentSerializer(serializers.ModelSerializer):
    students = StudentsSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ('lesson_id', 'date', 'description', 'students')


class SubscriptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriptions
        fields = ('account_id',)


class SubscriptionsStatusSerializer(serializers.ModelSerializer):
    # subscription_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Subscriptions.objects.all())

    class Meta:
        model = Subscriptions
        fields = ('subscription_id', 'status')


class SubscriptionsLessonSerializer(serializers.ModelSerializer):
    status = StatusSerializer(many=False)
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Subscriptions
        fields = ('subscription_id', 'status', 'lessons', 'subscription_date')



