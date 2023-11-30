# Generated by Django 4.2.6 on 2023-11-27 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_checkout'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkout',
            old_name='zip',
            new_name='zip_code',
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'), ('upi', 'UPI ID')], max_length=50)),
                ('checkout', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='order.checkout')),
            ],
        ),
    ]
