from django import forms
from .models import guest


# creating a form
class guestForm(forms.ModelForm):

    class Meta:
        model = guest

        fields = [
            "title",
            "description",
        ]
