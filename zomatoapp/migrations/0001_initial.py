# Generated by Django 4.2.4 on 2023-08-10 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('availability', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('received', 'Received'), ('preparing', 'Preparing'), ('ready', 'Ready for Pickup'), ('delivered', 'Delivered')], default='received', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zomatoapp.dish')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zomatoapp.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='dishes',
            field=models.ManyToManyField(through='zomatoapp.OrderItem', to='zomatoapp.dish'),
        ),
    ]