from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model


# ------------------------------------------------------------
# define user model
User = get_user_model()


# -------------------------------------------------------------------------
# serializers
class UserRegistrationSerializer(UserCreateSerializer):
    password: serializers.CharField = serializers.CharField(write_only=False)

    class Meta:
        model: User = User
        fields: list = ['email', 'first_name', 'last_name', 'password', 'phone', 'image']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model: User = User
        fields: list = ['first_name', 'last_name', 'phone', 'id', 'email', 'image']


class ChangePasswordSerializer(serializers.ModelSerializer):
    current_password: serializers.CharField = serializers.CharField()
    new_password: serializers.CharField = serializers.CharField()

    def validate(self, data):
        user = self.context['request'].user
        current_password = data.get('current_password')
        new_password = data.get('new_password')

        if not user.check_password(current_password):
            raise serializers.ValidationError('Wrong password')

        if new_password is not None and current_password == new_password:
            raise serializers.ValidationError('Similar password')
        return data

    class Meta:
        model: User = User
        fields: list = ['new_password', 'current_password']
