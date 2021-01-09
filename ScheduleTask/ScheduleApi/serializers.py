from rest_framework import serializers


class ScheduleApiSerializer(serializers.Serializer):
    date_time = serializers.DateTimeField(required=True)
    url = serializers.URLField(required=True)