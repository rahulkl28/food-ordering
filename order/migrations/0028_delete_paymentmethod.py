# Generated by Django 4.2.6 on 2023-11-29 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0027_alter_checkout_address_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PaymentMethod',
        ),
    ]
