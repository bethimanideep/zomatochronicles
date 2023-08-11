from django import forms
from .models import Dish

from django.core.validators import MinValueValidator, MaxValueValidator

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['dish_name', 'price', 'availability']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price


class OrderForm(forms.Form):
    customer_name = forms.CharField(max_length=100, required=True)
    dishes = forms.ModelMultipleChoiceField(
        queryset=Dish.objects.filter(availability=True),
        widget=forms.CheckboxSelectMultiple
    )


class UpdateStatusForm(forms.Form):
    STATUS_CHOICES = [
        ('received', 'Received'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready for Pickup'),
        ('delivered', 'Delivered'),
    ]
    
    new_status = forms.ChoiceField(choices=STATUS_CHOICES)

class UpdateStatusForm(forms.Form):
    STATUS_CHOICES = [
        ('received', 'Received'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready for Pickup'),
        ('delivered', 'Delivered'),
    ]
    
    new_status = forms.ChoiceField(choices=STATUS_CHOICES)