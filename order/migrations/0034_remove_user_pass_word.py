# Generated by Django 4.2.6 on 2023-12-06 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0033_alter_paymentmethod_checkout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='pass_word',
        ),
    ]