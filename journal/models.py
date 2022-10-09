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

    # Journal style entry
    title = models.CharField(max_length=50, null=True, blank=True)
    body = HTMLField(null=True, blank=True)

    # Quotation style entry
    quotation = models.TextField(max_length=200, null=True, blank=True)
    quotee = models.CharField(max_length=50, null=True, blank=True)

    bookmarked = models.BooleanField(default=False)
    entry_type = models.CharField(max_length=10, default='journal')


    class Meta:
        ordering = ['-created']
        verbose_name = "Entry"
        verbose_name_plural = "Entries"

    def __str__(self):
        return f'{self.author}-{self.created}'

    def get_absolute_url(self):
        return reverse('entry_detail', args=[str(self.id)])
