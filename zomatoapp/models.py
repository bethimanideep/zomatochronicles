from django.db import models

# Create your models here.
class Dish(models.Model):
    dish_name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    availability=models.BooleanField(default=True)
    def __str__(self):
        return self.dish_name

class Order(models.Model):
    customer_name=models.CharField(max_length=100)
    dishes=models.ManyToManyField(Dish,through='OrderItem')
    status_choices = [
        ('received', 'Received'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready for Pickup'),
        ('delivered', 'Delivered'),
    ]
    status=models.CharField(max_length=10,choices=status_choices,default='received')
    def __str__(self):
        return f"Order {self.pk} -{self.customer_name}"
    
    def calculate_total_price(self):
        total_price = sum(item.dish.price * item.quantity for item in self.orderitem_set.all())
        return total_price

    @property
    def total_price(self):
        return self.calculate_total_price()

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    dish=models.ForeignKey(Dish,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"Order {self.dish} -{self.quantity}"
