from django import forms


class PromocodeForm(forms.Form):
    promocode = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={
        'class': 'promocode-input', 'placeholder': 'Промокод'
    }))
