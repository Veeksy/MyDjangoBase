from django import forms


class ShopsForm(forms.Form):
    city = forms.CharField(label='Город', required=False)
    street = forms.CharField(label='Улица', required=False)
    status = forms.IntegerField(label='Статус', required=False)
