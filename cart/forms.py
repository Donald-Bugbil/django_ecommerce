from django import forms

quantity_choice = [(i, str(i)) for i in range(1, 21)]


class Quantity_select_form(forms.Form):

    quantity = forms.TypedChoiceField(
        choices=quantity_choice, coerce=int, label='')
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput)

    quantity.widget.attrs.update({
        'class': 'width'
    })
