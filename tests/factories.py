from datetime import datetime

import factory

from ads.models import Advertisement, Comment
from users.models import User


# ----------------------------------------------------------------
# instance factories
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker('email')
    password = 'test_password123'
    first_name = 'test_first_name'
    last_name = 'test_last_name'
    is_active = True
    phone = '+79111111111'


class AdvertisementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Advertisement

    title = 'test_advertisement'
    description = 'test_description'
    price = 999
    author = factory.SubFactory(UserFactory)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    text = 'test_comment'
    author = factory.SubFactory(UserFactory)
    ad = factory.SubFactory(AdvertisementFactory)
    created_at = None


