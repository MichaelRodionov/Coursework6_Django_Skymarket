from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.db.models import TextChoices

from users.managers import UserManager


# ----------------------------------------------------------------
# User model
class User(AbstractBaseUser):
    class Roles(TextChoices):
        ADMIN = 'admin', 'Администратор'
        USER = 'user', 'Пользователь'
    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS: list = ['first_name', 'last_name', 'phone', "role"]

    objects: UserManager = UserManager()

    first_name: models.CharField = models.CharField(max_length=150, blank=True)
    last_name: models.CharField = models.CharField(max_length=150, blank=True)
    email: models.EmailField = models.EmailField(unique=True, null=True)
    password: models.CharField = models.CharField(max_length=200)
    phone: models.CharField = models.CharField(max_length=20, null=True)
    role: models.CharField = models.CharField(max_length=15, choices=Roles.choices, default=Roles.USER)
    image: models.ImageField = models.ImageField(upload_to='images/', null=True)
    is_active: models.BooleanField = models.BooleanField(default=True)
    last_login: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name: str = 'Пользователь'
        verbose_name_plural: str = 'Пользователи'

    @property
    def is_superuser(self) -> bool:
        return self.is_admin

    @property
    def is_staff(self) -> bool:
        return self.is_admin

    def has_perm(self, perm, obj=None) -> bool:
        return self.is_admin

    def has_module_perms(self, app_label) -> bool:
        return self.is_admin

    @property
    def is_admin(self) -> bool:
        return self.role == User.Roles.ADMIN

    @property
    def is_user(self) -> bool:
        return self.role == User.Roles.USER

