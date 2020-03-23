from django import forms

from .models import Events, Puples

class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ("date", "name", "organization", "verification_file")

class AddEventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ("event_rate", "check",)
class ImgChangeForm(forms.ModelForm):
    class Meta:
        model = Puples
        fields = ("image",)