from rest_framework import serializers
from dashboard.models import Status, Subscriptions, Lesson
from account.models import Account, Students
from account.serializers import AccountIdSerializer, AccountSerializer


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Lesson
        fields = ('lesson_id', 'date', 'description')


class StatusIdSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Status
        fields = ('name', )

class SubscriptionsSerializer(serializers.HyperlinkedModelSerializer):
    account = AccountIdSerializer()
    # status = StatusIdSerializer()

    class Meta:
        model = Subscriptions
        fields = ('account',)

class SubscriptionsStatusSerializer(serializers.HyperlinkedModelSerializer):
    account = AccountIdSerializer()
    status = StatusIdSerializer()

    class Meta:
        model = Subscriptions
        fields = ('account', 'status')


class SubscriptionsLessonSerializer(serializers.HyperlinkedModelSerializer):
    # account = AccountSerializer(many=True, read_only=True)
    # status = StatusIdSerializer(many=True, read_only=True)
    # lesson = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Subscriptions
        fields = ('subscription_id', 'status', 'subscription_date', 'lesson')



