from django.forms import ModelForm

from .models import Entry


class EntryCreateForm(ModelForm):
    """Form used to create a new journal entry"""

    class Meta:
        model = Entry

        fields = (
            'title',
            'body',
        )

        labels = {
            'title': 'Title',
            'body': 'Body',
        }

        help_texts = {
            'title': 'Optional, 1-50 characters',
            'body': 'Required',
        }


class EntryUpdateForm(EntryCreateForm):
    """Form used to update a journal entry"""
