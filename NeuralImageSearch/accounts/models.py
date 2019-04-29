from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), max_length=254)
    age = models.IntegerField(_("age"), blank=True, null=True, default=18)

    def __str__(self):
        return self.email