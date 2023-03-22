from django.db.models import Model, ImageField, CharField, ForeignKey, CASCADE, DateTimeField, PositiveIntegerField, \
    TextField


# ----------------------------------------------------------------
# advertisement model
class Advertisement(Model):
    image = ImageField(upload_to='images/', null=True)
    title = CharField(max_length=50)
    price = PositiveIntegerField()
    author = ForeignKey('users.User', on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    description = TextField(max_length=2000, null=True)

    class Meta:
        verbose_name: str = 'Объявление'
        verbose_name_plural: str = 'Объявления'


# ----------------------------------------------------------------
# comment model
class Comment(Model):
    text = CharField(max_length=500)
    author = ForeignKey('users.User', on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    ad = ForeignKey(Advertisement, on_delete=CASCADE)

    class Meta:
        verbose_name: str = 'Комментарий'
        verbose_name_plural: str = 'Комментарии'

