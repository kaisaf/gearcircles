from django import forms

PAYMENT_CHOICES = (
    (0, 'Cash'),
    (1, 'Paypal'),
    (2, 'Any')
)

class RentalForm(forms.Form):
    start_date = forms.DateField(label='Start Date')
    end_date = forms.DateField(label='End Date')
    payment = forms.ChoiceField(choices=PAYMENT_CHOICES)
