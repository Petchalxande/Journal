from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
import uuid

from tinymce.models import HTMLField


class Entry(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    body = HTMLField()
    bookmarked = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']
        verbose_name = "Entry"
        verbose_name_plural = "Entries"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('entry_detail', args=[str(self.id)])
