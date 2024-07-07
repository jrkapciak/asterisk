import uuid
from typing import Any

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    """
    An abstract base class model that provides UUID field and self updating
    ``created_at`` and ``updated_at``.
    """

    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(verbose_name=_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("updated at"), auto_now=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.uuid}"

    def save(self, *args: Any, **kwargs: Any) -> None:
        if "update_fields" in kwargs:
            kwargs["update_fields"] = list(set(list(kwargs["update_fields"]) + ["updated_at"]))
        return super().save(*args, **kwargs)
