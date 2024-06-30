from django import forms


class PromocodeForm(forms.Form):
    promocode = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={
        'class': 'promocode-input', 'placeholder': 'Промокод'
    }))


class SortForm(forms.Form):
    sort_by = forms.ChoiceField(
        choices=[('default', 'Сортировка'), ('price_increase', 'По возрастанию цены'),
                 ('price_drop', 'По убыванию цены')],
        label=False,
        widget=forms.Select(attrs={'onchange': 'this.form.submit();', 'class': 'sort_form'})
    )
