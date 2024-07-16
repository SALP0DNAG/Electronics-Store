from django import forms


class PromocodeForm(forms.Form):
    promocode = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={
        'class': 'promocode-input', 'placeholder': 'Промокод'
    }))


class SortFormProducts(forms.Form):
    sort_by = forms.ChoiceField(
        choices=[('default', 'Сортировка'),
                 ('price_drop', 'По убыванию цены'),
                 ('price_increase', 'По возрастанию цены'),
                 ],
        label=False,
        widget=forms.Select(attrs={'onchange': 'this.form.submit();', 'class': 'sort_form'})
    )


class SortFormFavorites(forms.Form):
    sort_by = forms.ChoiceField(
        choices=[('default', 'Сортировка'),
                 ('price_drop', 'По убыванию цены'),
                 ('price_increase', 'По возрастанию цены'),
                 ('data_addition', 'По дате добавления')
                 ],
        label=False,
        widget=forms.Select(attrs={'onchange': 'this.form.submit();', 'class': 'sort_form'})
    )


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'Поиск'}))
