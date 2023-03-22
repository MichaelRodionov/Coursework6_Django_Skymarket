from rest_framework import serializers

from ads.models import *


# ----------------------------------------------------------------
# comment serializer
class CommentSerializer(serializers.ModelSerializer):
    """Serializer for DetailAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView of comments"""
    author_id = serializers.IntegerField()
    ad_id = serializers.IntegerField()
    author_first_name = serializers.CharField(source='author.first_name', required=False)
    author_last_name = serializers.CharField(source='author.last_name', required=False)
    author_image = serializers.ImageField(source='author.image', read_only=True)

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
        fields: list[str] = [
            'pk', 'text', 'author_id', 'created_at', 'author_first_name', 'author_last_name', 'ad_id', 'author_image'
        ]


# ----------------------------------------------------------------
# Advertisement serializer
class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer for full CRUD"""
    author_id = serializers.IntegerField(required=False)
    author_first_name = serializers.CharField(source='author.first_name', required=False)
    author_last_name = serializers.CharField(source='author.last_name', required=False)
    phone = serializers.CharField(source='author.phone', required=False)

    def is_valid(self, raise_exception=False) -> bool:
        """Method to check initial data"""
        if not self.initial_data.get('author_id'):
            self.initial_data['author_id'] = self.context['request'].user.id
        return super().is_valid(raise_exception=raise_exception)

    class Meta:
        model: Advertisement = Advertisement
        fields: list = ['pk', 'image', 'title', 'price', 'phone', 'description', 'author_first_name',
                        'author_last_name', 'author_id']

