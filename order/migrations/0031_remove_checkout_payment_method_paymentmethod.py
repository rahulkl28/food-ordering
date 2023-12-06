# Generated by Django 4.2.6 on 2023-11-29 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0030_checkout_payment_method_delete_paymentmethod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='payment_method',
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('credit_card', 'Credit Card'), ('debit_card', 'Debit Card')], default='credit_card', max_length=50)),
                ('checkout', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment_method', to='order.checkout')),
            ],
        ),
    ]