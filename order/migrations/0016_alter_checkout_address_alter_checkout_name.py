# Generated by Django 4.2.6 on 2023-11-27 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_alter_checkout_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='address',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
