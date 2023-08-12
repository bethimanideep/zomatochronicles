from django.db import models
from django import forms
from .models import Dish 

from django.core.validators import MinValueValidator, MaxValueValidator

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['dish_name', 'price', 'availability', 'image_url']
        widgets = {
            'image_url': forms.URLInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'dish_name': 'Dish Name',
            'price': 'Price',
            'availability': 'Availability',
            'image_url': 'Image URL',
        }


    def __str__(self):
        return self.dish_name



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