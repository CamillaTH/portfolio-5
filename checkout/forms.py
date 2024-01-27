from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'phone', 'postal_code',
                  'country', 'city', 'street_address',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'needs-validation'
        self.helper.add_input(Submit('submit', 'Submit'))

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
            self.fields[field].widget.attrs['placeholder'] = placeholders[field]
            self.fields[field].widget.attrs['class'] = 'form-control'

        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='col-md-6'),
                Column('last_name', css_class='col-md-6'),
            ),
            Row(
                Column('email', css_class='col-md-6'),
                Column('phone', css_class='col-md-6'),
            ),
            'postal_code',
            'country',
            'city',
            'street_address',
        )