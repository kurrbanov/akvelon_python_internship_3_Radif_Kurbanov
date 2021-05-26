from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomeUser
        fields = ['id', 'first_name', 'last_name', 'email']

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'user_id', 'amount', 'date']

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.date = validated_data.get('date', instance.get)
        instance.save()
        return instance


class OutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outcome
        fields = ['id', 'user_id', 'amount', 'date']

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.date = validated_data.get('date', instance.get)
        instance.save()
        return instance
