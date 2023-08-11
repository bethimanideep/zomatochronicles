from django.shortcuts import render, redirect
from .models import Dish, Order, OrderItem 
from .forms import DishForm ,OrderForm ,UpdateStatusForm
from django.shortcuts import get_object_or_404

def homepage(request):
    print("hi")
    return render(request, "menu/homepage.html")

def cancel_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.delete()
    return redirect('menu:updatestatus')


def updatestatus(request):
    orders = Order.objects.all()
    filter_status = request.POST.get('filter_status', '')

    if request.method == 'POST':
        if 'update_order' in request.POST:
            for order in orders:
                order_pk = str(order.pk)
                new_status = request.POST.get(f'status_{order_pk}')
                if new_status:
                    order.status = new_status
                    order.save()

    if filter_status:
        orders = orders.filter(status=filter_status)

    return render(request, 'menu/updatestatus.html', {'orders': orders, 'filter_status': filter_status})


def load_order_form(request):
    form = OrderForm()
    dishes = Dish.objects.filter(availability=True)
    return render(request, 'menu/take_order.html', {'form': form, 'dishes': dishes})

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            customer_name = form.cleaned_data['customer_name']
            order = Order.objects.create(customer_name=customer_name)
            for dish in form.cleaned_data['dishes']:
                quantity_field_name = f'quantity_{dish.pk}'
                quantity = int(request.POST.get(quantity_field_name, 0))
                if quantity > 0:
                    OrderItem.objects.create(order=order, dish=dish, quantity=quantity)
                    
                orders = Order.objects.all()
                filter_status = request.POST.get('filter_status', '')
                return render(request, 'menu/updatestatus.html', {'orders': orders, 'filter_status': filter_status})
    return redirect('menu:load_order_form')  # Redirect back to the form page if form is not valid or GET request




def menu_list(request):
    dishes = Dish.objects.all()
    return render(request, 'menu/menu_list.html', {'dishes': dishes})

def add_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu:menu_list')
    else:
        form = DishForm()
    return render(request, 'menu/add_dish.html', {'form': form})

def edit_dish(request, dish_id):
    dish = Dish.objects.get(pk=dish_id)
    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('menu:menu_list')
    else:
        form = DishForm(instance=dish)
    return render(request, 'menu/edit_dish.html', {'form': form, 'dish': dish})

def delete_dish(request, dish_id):
    dish = Dish.objects.get(pk=dish_id)
    if request.method == 'POST':
        dish.delete()
        return redirect('menu:menu_list')
    return render(request, 'menu/delete_dish.html', {'dish': dish})


