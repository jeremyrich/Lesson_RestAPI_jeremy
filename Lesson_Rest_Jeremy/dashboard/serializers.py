from rest_framework import serializers
from dashboard.models import Status, Subscriptions, Lesson
from account.models import Account, Students
from account.serializers import AccountSerializer


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Lesson
        fields = ('lesson_id', 'date', 'description')


class StatusSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Status
        fields = ('status_id','name' )

class SubscriptionsStatusSerializer(serializers.HyperlinkedModelSerializer):
    account = AccountSerializer(many=True, read_only=True)
    status = StatusSerializer(many=True, read_only=True)

    class Meta:
        model = Subscriptions
        fields = ('account', 'status')


class SubscriptionsLessonSerializer(serializers.HyperlinkedModelSerializer):
    # account = AccountSerializer(many=True, read_only=True)
    status = StatusSerializer(many=True, read_only=True)
    lesson = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Subscriptions
        fields = ('subscription_id', 'status', 'subscription_date', 'lesson')



