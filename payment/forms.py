from django import forms 

class PaymentForm(forms.Form):
    MTN = "Mtn"

    LIST_OF_NETWORK =[
        (MTN, 'Mtn')
    ]

    phone_number  = forms.CharField(max_length=10)
    network = forms.ChoiceField(choices=LIST_OF_NETWORK)
