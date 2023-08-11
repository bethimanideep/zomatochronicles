from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('menu/', views.menu_list, name='menu_list'),
    path('menu/add/', views.add_dish, name='add_dish'),
    path('menu/edit/<int:dish_id>/', views.edit_dish, name='edit_dish'),
    path('menu/delete/<int:dish_id>/', views.delete_dish, name='delete_dish'),
    path('menu/updatestatus/', views.updatestatus, name='updatestatus'),
    path('menu/take_order/', views.load_order_form, name='load_order_form'),
    path('menu/place_order/', views.place_order, name='place_order'),
    path('menu/cancel_order/<int:order_id>/', views.cancel_order, name='cancel_order'),
]
