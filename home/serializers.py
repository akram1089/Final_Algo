from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'






# serializers.py

from rest_framework import serializers

class TemplateSerializer(serializers.Serializer):
    content = serializers.CharField()





