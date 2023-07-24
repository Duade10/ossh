from django import forms
from .models import Registration, Event


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = [
            "event",
            "full_name",
            "organization",
            "participant_type",
            "number_of_participants",
            "email_address",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
            self.fields["event"].widget.attrs["disabled"] = True
            self.fields
