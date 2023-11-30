# Generated by Django 4.2.6 on 2023-11-29 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0022_alter_checkout_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='address',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='address_location',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='email',
            field=models.EmailField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='zip_code',
            field=models.IntegerField(null=True),
        ),
    ]
