from django.test import TestCase

from .forms import OrderForm
from .models import Order

class OrderFormTest(TestCase):
    def test_form_fields(self):
        form = OrderForm()
        self.assertEqual(form.Meta.model, Order)

    def test_form_widget_attributes(self):
        form = OrderForm()
        self.assertEqual(form.fields['first_name'].widget.attrs['placeholder'], 'First name *')
    

    def test_form_required_fields(self):
        form = OrderForm()

        self.assertTrue(form.fields['first_name'].required)
        self.assertTrue(form.fields['email'].required)