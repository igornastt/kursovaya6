from django import forms
from mailing.models import Mail
from clients.models import Client
from mailing.utils import get_current_request


class StyleFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailCreateForm(forms.ModelForm):

    class Meta:
        model = Mail
        fields = ('title', 'content', 'sending_time', 'sending_period', 'start_date', 'end_date', 'clients')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = get_current_request()
        self.fields['clients'].queryset = Client.objects.filter(owner=request.user)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailUpdateForm(forms.ModelForm):

    class Meta:
        model = Mail
        fields = ('title', 'content', 'clients')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = get_current_request()
        self.fields['clients'].queryset = Client.objects.filter(owner=request.user)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            