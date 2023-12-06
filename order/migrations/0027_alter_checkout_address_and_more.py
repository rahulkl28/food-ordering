# Generated by Django 4.2.6 on 2023-11-29 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0026_alter_checkout_address_alter_checkout_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='address',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='address_location',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='email',
            field=models.EmailField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='zip_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]