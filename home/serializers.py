# serializers.py
from rest_framework import serializers

class WebhookPayloadSerializer(serializers.Serializer):
    orderNumber = serializers.IntegerField()
    sell_buy_indicator = serializers.CharField(max_length=10)