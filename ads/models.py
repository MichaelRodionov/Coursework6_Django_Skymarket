from django.core.validators import MinValueValidator
from django.db.models import Model, ImageField, CharField, IntegerField, ForeignKey, CASCADE, DateTimeField


# ----------------------------------------------------------------
# advertisement model
class Advertisement(Model):
    image = ImageField(upload_to='images/', null=True)
    title = CharField(max_length=50)
    price: IntegerField = IntegerField(validators=[MinValueValidator(0)])
    author: ForeignKey = ForeignKey('users.User', on_delete=CASCADE)
    created_at: DateTimeField = DateTimeField(auto_now_add=True)
    description: CharField = CharField(max_length=1000, null=True)

    class Meta:
        verbose_name: str = 'Объявление'
        verbose_name_plural: str = 'Объявления'


# ----------------------------------------------------------------
# comment model
class Comment(Model):
    text: CharField = CharField(max_length=200)
    author: ForeignKey = ForeignKey('users.User', on_delete=CASCADE)
    created_at: DateTimeField = DateTimeField(auto_now_add=True)
    ad = ForeignKey(Advertisement, on_delete=CASCADE)

    class Meta:
        verbose_name: str = 'Комментарий'
        verbose_name_plural: str = 'Комментарии'

