from django.db import models
from django.contrib.auth.models import AbstractUser

from django.urls import reverse
from django.utils.translation import gettext_lazy
import uuid



class CustomUser(AbstractUser):
  
  #auth
  id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
  username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
  email = models.EmailField(gettext_lazy('email address'), unique = True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

  class Meta:
    ordering = ['first_name',]
    verbose_name = "User"
    verbose_name_plural = "Users"

  def __str__(self):
    return self.email

  def get_absolute_url(self):
    return reverse('user')



