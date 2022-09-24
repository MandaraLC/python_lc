import datetime

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import ScrapeTask, ScrapeConfigAccount, ScrapeResult


class ScrapeTaskSerializer(serializers.ModelSerializer):

    def validate_early_etd(self, value):
        if value < datetime.datetime.now():
            raise ValidationError('最早出发时间不能比当前时间小')
        return value

    def validate(self, attrs):
        if attrs['early_etd'] > attrs['late_etd']:
            raise ValidationError('最晚出发时间不能比最早出发时间小')

        if attrs['min_price'] > attrs['max_price']:
            raise ValidationError('最高价格不能小于最低价格')

        return attrs

    class Meta:
        model = ScrapeTask
        exclude = ['create_time', 'update_time']


class ScrapeAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScrapeConfigAccount
        exclude = ['create_time', 'update_time']


class ScrapeResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScrapeResult
        exclude = ['create_time', 'update_time']
