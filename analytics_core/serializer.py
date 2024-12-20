from rest_framework import serializers


class CreateAnalyticsRowSerializer(serializers.Serializer):
    network_name = serializers.CharField(max_length=255)
    city_name = serializers.CharField(max_length=255)
    company_name = serializers.CharField(max_length=255)
    salon_name = serializers.CharField(max_length=255)
    manager_name = serializers.CharField(max_length=255)
    deal_amount = serializers.FloatField(default=0.0)
    from_status = serializers.CharField(max_length=255, default="EMPTY")
    to_status = serializers.CharField(max_length=255)
    external_id = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()
