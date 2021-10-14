from django.views import generic

from . import forms, mixins, models


class BidAjaxCreateView(
        mixins.AjaxFormMixin,
        generic.CreateView,
):
    model = models.Bid
    form_class = forms.BidForm
    prefix = 'bid'

    def mail_object(self):
        self.object.mail_admin()
