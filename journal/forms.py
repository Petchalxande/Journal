from django.forms import ModelForm

from .models import Entry


class EntryCreateForm(ModelForm):
    """Form used to create a new journal entry"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['body'].required = True

    class Meta:
        model = Entry

        fields = (
            'title',
            'body',
        )

        labels = {
            'title': 'Title',
            'body': 'Content',
        }

        help_texts = {
            'title': 'Required, 1-50 characters',
            'body': 'Required',
        }


class EntryUpdateForm(EntryCreateForm):
    """Form used to update a journal entry"""


class QuotationCreateForm(ModelForm):
    """Form used to create a new quote style entry"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quotation'].required = True
        self.fields['quotee'].required = True

    class Meta:
        model = Entry

        fields = (
            'quotation',
            'quotee',
        )

        labels = {
            'quotation': 'Quotation',
            'quotee': 'Source',
        }

        help_texts = {
            'quotation': 'Required, 1-200 characters',
            'quotee': 'Required, 1-50 characters',
        }


class QuotationUpdateForm(QuotationCreateForm):
    """Form used to update a quote style entry"""
