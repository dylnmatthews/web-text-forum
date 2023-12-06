from rest_framework import serializers
from .models import Like
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']

    def validate(self, data):
        user = data['user']
        post = data['post']

        if user == post.user:
            raise serializers.ValidationError("A user cannot like their own post.")

        return data

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except Exception as e:
            return str(e)
    
    def save(self, **kwargs):
        super().save(**kwargs)
        return None