from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'phone', 'postal_code',
                  'country', 'city', 'street_address',)

    def __init__(self, *args, **kwargs):
        ''' set fields when init '''

        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email address',
            'phone': 'Mobile phone',
            'postal_code': 'Postal code',
            'country': 'Country',
            'city': 'City',
            'street_address': 'Street address',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]

            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False