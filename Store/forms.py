from django import forms


class PromocodeForm(forms.Form):
    promocode = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={
        'class': 'promocode-input', 'placeholder': 'Промокод'
    }))


class SortForm(forms.Form):
    CHOICES = (('Option 1', 'Сортировка'), ('Option 2', 'Option 2'),)
    sort_by = forms.CharField(widget=forms.Select(choices=CHOICES, attrs={'onchange': 'this.form.submit();'}))
