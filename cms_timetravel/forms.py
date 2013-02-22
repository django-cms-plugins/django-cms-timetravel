from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
from django.utils.translation import ugettext as _


class TimetravelForm(forms.Form):
    timetravel_date = forms.DateTimeField(label=_('Timetravel date'), widget=AdminSplitDateTime())
    auto_redirect = forms.BooleanField(label=_('Automatically to the homepage'), required=False)
