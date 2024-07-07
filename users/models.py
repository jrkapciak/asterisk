from typing import Any, Optional

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from common.models import BaseModel


class UserManager(BaseUserManager["User"]):
    use_in_migrations = True

    def _create_user(self, email: str, password: Optional[str] = None, **extra_fields: dict[str:Any]) -> "User":
        if not email:
            raise ValueError("Users require an email field")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, password: Optional[str] = None, **extra_fields: dict[str:Any]) -> "User":
        extra_fields.setdefault("is_staff", False)  # type: ignore
        extra_fields.setdefault("is_superuser", False)  # type: ignore
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email: str, password: Optional[str] = None, **extra_fields: dict[str:Any]) -> "User":
        extra_fields.setdefault("is_staff", True)  # type: ignore
        extra_fields.setdefault("is_superuser", True)  # type: ignore

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def active(self) -> models.QuerySet["User"]:
        return self.get_queryset().filter(is_active=True)


class User(AbstractUser, BaseModel):
    mobile_phone = PhoneNumberField(blank=True, verbose_name=_("Mobile phone number"))
    email = models.EmailField(_("email address"), unique=True)

    objects = UserManager()  # type: ignore

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower("email"),
                name="user_email_ci_uniqueness",
            ),
        ]
