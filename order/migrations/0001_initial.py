# Generated by Django 4.2.6 on 2023-10-31 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=10)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('your_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('persons_number', models.IntegerField(blank=True, null=True)),
                ('your_message', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
