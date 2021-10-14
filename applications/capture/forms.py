from django import forms

from . import models


class PhoneMaskMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'data-mask': '+7 (000) 000 00-00'})


class BidForm(
        PhoneMaskMixin,
        forms.ModelForm,
):
    class Meta:
        model = models.Bid
        fields = [
            'name',
            'phone',
            'email',
        ]
