""" Data Serializers """
#Models
from api.models import Dataset, Row
#Django REST Framework
from rest_framework import serializers

class DataSerializer(serializers.ModelSerializer):
    """Model Data Serializer"""
    class Meta:
        model = Dataset
        fields = ('name', 'upload', 'date')


class RowSerializer(serializers.ModelSerializer):
    """Model Row Serializer"""
    class Meta:
        model = Row
        fields = '__all__'
