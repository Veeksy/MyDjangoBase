from django import forms


class ShopsForm(forms.Form):
    name = forms.CharField(max_length=50)
    street = forms.IntegerField()
    house = forms.IntegerField()
    time_to_close = forms.TimeField()
    time_to_open = forms.TimeField()