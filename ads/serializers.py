from typing import Any

from rest_framework import serializers

from ads.models import *
from users.serializers import UserSerializer


# ----------------------------------------------------------------
# comment serializer
class CommentSerializer(serializers.ModelSerializer):
    """Serializer for DetailAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView of comments"""
    author_id: serializers.IntegerField = serializers.IntegerField()
    ad_id: serializers.IntegerField = serializers.IntegerField()
    author_first_name: serializers.SerializerMethodField = serializers.SerializerMethodField()
    author_last_name: serializers.SerializerMethodField = serializers.SerializerMethodField()
    author_image: serializers.SerializerMethodField = serializers.SerializerMethodField(read_only=True)

    def get_author_first_name(self, com) -> Any:
        request: Any = self.context.get('request')
        serializer: UserSerializer = UserSerializer(instance=com.author, context={'request': request})
        return serializer.data.get('first_name')

    def get_author_last_name(self, com) -> Any:
        request: Any = self.context.get('request')
        serializer: UserSerializer = UserSerializer(instance=com.author, context={'request': request})
        return serializer.data.get('last_name')

    def get_author_image(self, com) -> Any:
        request: Any = self.context.get('request')
        serializer: UserSerializer = UserSerializer(instance=com.author, context={'request': request})
        return serializer.data.get('image')

    def is_valid(self, raise_exception=False) -> bool:
        """Method to check initial data"""
        self.initial_data['author_id'] = self.context['request'].user.id
        self.initial_data['ad_id'] = self.context['request'].parser_context['kwargs']['ad_pk']
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data) -> Comment:
        """Method to create instance of comment"""
        return Comment.objects.create(**validated_data)

    class Meta:
        model: Comment = Comment
        fields: list = [
            'pk', 'text', 'author_id', 'created_at', 'author_first_name', 'author_last_name', 'ad_id', 'author_image'
        ]


# ----------------------------------------------------------------
# Advertisement serializer
class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer for full CRUD"""
    author_id: serializers.IntegerField = serializers.IntegerField(required=False)
    author_first_name: serializers.SerializerMethodField = serializers.SerializerMethodField()
    author_last_name: serializers.SerializerMethodField = serializers.SerializerMethodField()
    phone: serializers.SerializerMethodField = serializers.SerializerMethodField()

    def get_author_first_name(self, ad) -> Any:
        return ad.author.first_name

    def get_author_last_name(self, ad) -> Any:
        return ad.author.last_name

    def get_phone(self, ad) -> Any:
        return ad.author.phone

    def is_valid(self, raise_exception=False) -> bool:
        """Method to check initial data"""
        if not self.initial_data.get('author_id'):
            self.initial_data['author_id'] = self.context['request'].user.id
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data) -> Advertisement:
        """Method to create instance of advertisement"""
        return Advertisement.objects.create(**validated_data)

    class Meta:
        model: Advertisement = Advertisement
        fields: list[str] = ['pk', 'image', 'title', 'price', 'phone', 'description', 'author_first_name',
                             'author_last_name', 'author_id']

