from rest_framework import serializers
from .models import User, Record

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'is_active']

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'
        read_only_fields = ['user']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be positive")
        return value
    

